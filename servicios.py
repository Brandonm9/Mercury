# servicios.py

from sqlalchemy import text
from app import db
from modelos import Sucursal

def obtener_alertas_stock(sucursal_id):
    """
    Llama al stored procedure sp_GetAlertasPorSucursal y devuelve
    las alertas de stock bajo de la sucursal indicada.
    """
    sql = text("EXEC sp_GetAlertasPorSucursal :sucursal_id")
    result = db.session.execute(sql, {'sucursal_id': sucursal_id})
    return result.mappings().all()

def obtener_productos_sucursal(sucursal_id, busqueda=None):
    """
    Llama al stored procedure sp_GetProductosPorSucursal y opcionalmente
    filtra por nombre de producto.
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

    return productos

def ventas_por_sucursal(sucursal_id):
    """
    Devuelve las ventas diarias (fecha, total) de la sucursal indicada.
    """
    sql = text("""
        SELECT
            CAST(m.fecha AS DATE) AS fecha,
            SUM(m.cantidad)       AS total
        FROM Movimiento m
        JOIN ProductoSucursal ps ON m.producto_sucursal_id = ps.id
        WHERE m.tipo = 'salida'
          AND ps.sucursal_id = :sucursal_id
        GROUP BY CAST(m.fecha AS DATE)
        ORDER BY CAST(m.fecha AS DATE)
    """)
    result = db.session.execute(sql, {'sucursal_id': sucursal_id})
    return [dict(r) for r in result.mappings().all()]

def ventas_por_vendedor(sucursal_id):
    """
    Lee la vista vw_VentasPorVendedor y filtra solo los vendedores
    de la sucursal indicada.
    """
    sql = text("""
        SELECT v.usuario_id, v.vendedor, v.total
        FROM vw_VentasPorVendedor v
        JOIN Usuario u ON v.usuario_id = u.id
        WHERE u.sucursal_id = :sucursal_id
        ORDER BY v.vendedor
    """)
    result = db.session.execute(sql, {'sucursal_id': sucursal_id})
    return [dict(r) for r in result.mappings().all()]

def obtener_sucursales():
    """
    Recupera el listado de sucursales para construir menús desplegables.
    """
    sql = text("SELECT id, nombre FROM Sucursal ORDER BY nombre")
    result = db.session.execute(sql)
    return result.mappings().all()

def obtener_todos_los_productos_para_admin():
    """
    Inventario global para Administrador: sucursal, producto, stock_actual, stock_minimo.
    """
    sql = text("""
        SELECT
            s.id           AS sucursal_id,
            s.nombre       AS sucursal,
            p.id           AS producto_id,
            p.nombre       AS producto,
            ps.stock_actual,
            ps.stock_minimo
        FROM ProductoSucursal ps
        JOIN Sucursal s ON ps.sucursal_id = s.id
        JOIN Producto p ON ps.producto_id = p.id
        ORDER BY s.nombre, p.nombre
    """)
    result = db.session.execute(sql)
    return [dict(r) for r in result.mappings().all()]

def obtener_auditoria(sucursal_id=None):
    """
    Registros de auditoría. Si se pasa sucursal_id, filtra por usuarios de esa sucursal.
    """
    sql = text("""
        SELECT
            a.id,
            u.nombre        AS usuario,
            u.sucursal_id   AS sucursal_id,
            a.accion,
            a.tabla_afectada,
            a.fecha
        FROM Auditoria a
        JOIN Usuario u ON a.usuario_id = u.id
        WHERE (:sucursal_id IS NULL OR u.sucursal_id = :sucursal_id)
        ORDER BY a.fecha DESC
    """)
    result = db.session.execute(sql, {'sucursal_id': sucursal_id})
    return result.mappings().all()
