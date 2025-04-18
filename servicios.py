# servicios.py

from sqlalchemy import text
from modelos import db

def obtener_alertas_stock(sucursal_id):
    """
    Retorna las alertas de stock bajo para una sucursal.
    """
    sql = text("""
        SELECT 
            ps.id AS producto_sucursal_id,
            pr.nombre AS producto,
            ps.stock_actual,
            ps.stock_minimo,
            CONCAT('Stock bajo en sucursal ', ps.sucursal_id, ': ', ps.stock_actual, ' <= ', ps.stock_minimo) AS mensaje
        FROM ProductoSucursal ps
        JOIN Producto pr ON ps.producto_id = pr.id
        WHERE ps.sucursal_id = :sucursal_id
          AND ps.stock_actual <= ps.stock_minimo
    """)
    result = db.session.execute(sql, {'sucursal_id': sucursal_id})
    return [dict(r) for r in result.mappings().all()]

def obtener_productos_sucursal(sucursal_id, busqueda=None):
    """
    Llama al stored procedure sp_GetProductosPorSucursal y opcionalmente filtra por nombre.
    """
    sql = text("EXEC sp_GetProductosPorSucursal :sucursal_id")
    result = db.session.execute(sql, {'sucursal_id': sucursal_id})
    productos = result.mappings().all()

    if busqueda:
        palabra = busqueda.strip().lower()
        productos = [
            p for p in productos
            if palabra in p['producto'].lower()
        ]

    return [dict(p) for p in productos]

def ventas_por_sucursal(sucursal_id):
    """
    Retorna ventas diarias (tipo 'salida') de una sucursal.
    """
    sql = text("""
        SELECT 
            CONVERT(date, m.fecha) AS fecha,
            SUM(m.cantidad) AS total
        FROM Movimiento m
        JOIN ProductoSucursal ps ON m.producto_sucursal_id = ps.id
        WHERE ps.sucursal_id = :sucursal_id
          AND m.tipo = 'salida'
        GROUP BY CONVERT(date, m.fecha)
        ORDER BY CONVERT(date, m.fecha)
    """)
    result = db.session.execute(sql, {'sucursal_id': sucursal_id})
    return [
        {'fecha': str(r['fecha']), 'total': r['total']}
        for r in result.mappings().all()
    ]

def ventas_por_vendedor(sucursal_id):
    """
    Retorna ventas totales por vendedor dentro de una sucursal.
    """
    sql = text("""
        SELECT 
            m.usuario_id,
            u.nombre AS vendedor,
            SUM(m.cantidad) AS total
        FROM Movimiento m
        JOIN Usuario u ON m.usuario_id = u.id
        JOIN ProductoSucursal ps ON m.producto_sucursal_id = ps.id
        WHERE ps.sucursal_id = :sucursal_id
          AND m.tipo = 'salida'
        GROUP BY m.usuario_id, u.nombre
    """)
    result = db.session.execute(sql, {'sucursal_id': sucursal_id})
    return [dict(r) for r in result.mappings().all()]

def ventas_por_fecha(sucursal_id, fecha_inicio, fecha_fin):
    """
    Retorna ventas diarias (tipo 'salida') de una sucursal
    entre dos fechas (inclusive).
    """
    sql = text("""
        SELECT 
            CONVERT(date, m.fecha) AS fecha,
            SUM(m.cantidad)      AS total
        FROM Movimiento m
        JOIN ProductoSucursal ps ON m.producto_sucursal_id = ps.id
        WHERE ps.sucursal_id = :sucursal_id
          AND m.tipo = 'salida'
          AND CONVERT(date, m.fecha) BETWEEN :fecha_inicio AND :fecha_fin
        GROUP BY CONVERT(date, m.fecha)
        ORDER BY CONVERT(date, m.fecha)
    """)
    params = {
        'sucursal_id': sucursal_id,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin
    }
    result = db.session.execute(sql, params)
    return [
        {'fecha': str(r['fecha']), 'total': r['total']}
        for r in result.mappings().all()
    ]

def obtener_sucursales():
    """
    Lista todas las sucursales (para el menú del administrador).
    """
    sql = text("SELECT id, nombre FROM Sucursal ORDER BY nombre")
    result = db.session.execute(sql)
    return [dict(r) for r in result.mappings().all()]

def obtener_auditoria(id_sucursal=None):
    """
    Trae el registro de auditoría. El parámetro id_sucursal se ignora
    porque la tabla Auditoria no referencia sucursales directamente.
    """
    sql = text("""
        SELECT 
            a.id,
            a.fecha,
            u.nombre      AS usuario,
            a.accion,
            a.tabla_afectada
        FROM Auditoria a
        JOIN Usuario u ON a.usuario_id = u.id
        ORDER BY a.fecha DESC
    """)
    result = db.session.execute(sql)
    return [dict(r) for r in result.mappings().all()]

def obtener_todos_los_productos_para_admin():
    """
    Lista todos los productos con su stock por sucursal.
    """
    sql = text("""
        SELECT 
            s.id       AS sucursal_id,
            s.nombre   AS sucursal,
            pr.nombre  AS producto,
            ps.stock_actual,
            ps.stock_minimo
        FROM ProductoSucursal ps
        JOIN Sucursal s  ON ps.sucursal_id = s.id
        JOIN Producto pr ON ps.producto_id   = pr.id
        ORDER BY s.nombre, pr.nombre
    """)
    result = db.session.execute(sql)
    return [dict(r) for r in result.mappings().all()]
