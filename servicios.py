# servicios.py
from app import db
from modelos import ProductoSucursal, Movimiento, Usuario
from sqlalchemy import func, cast, Date, text


def obtener_alertas_stock(sucursal_id):
    """
    Devuelve lista de ProductoSucursal con stock_actual <= stock_minimo para una sucursal.
    """
    return ProductoSucursal.query.filter(
        ProductoSucursal.sucursal_id == sucursal_id,
        ProductoSucursal.stock_actual <= ProductoSucursal.stock_minimo
    ).all()


def ventas_por_sucursal(sucursal_id):
    """
    Retorna datos de ventas diarias (sumatoria de 'salida') para gráficas.
    Devuelve una lista de diccionarios: [{'fecha': 'YYYY-MM-DD', 'total': cantidad}, ...]
    """
    resultados = (
        db.session.query(
            cast(Movimiento.fecha, Date).label('fecha'),
            func.sum(Movimiento.cantidad).label('total')
        )
        .join(ProductoSucursal, Movimiento.producto_sucursal_id == ProductoSucursal.id)
        .filter(
            Movimiento.tipo == 'salida',
            ProductoSucursal.sucursal_id == sucursal_id
        )
        .group_by(cast(Movimiento.fecha, Date))
        .order_by(cast(Movimiento.fecha, Date))
        .all()
    )
    return [{'fecha': str(r.fecha), 'total': r.total} for r in resultados]



def ventas_por_vendedor(sucursal_id):
    """
    Lee la vista vw_VentasPorVendedor y filtra sólo los vendedores
    de la sucursal indicada.
    Devuelve lista de dicts {'usuario_id','vendedor','total'}.
    """
    sql = text("""
        SELECT v.usuario_id, v.vendedor, v.total
        FROM vw_VentasPorVendedor v
        JOIN Usuario u ON v.usuario_id = u.id
        WHERE u.sucursal_id = :suc_id
        ORDER BY v.vendedor
    """)
    result = db.session.execute(sql, {'suc_id': sucursal_id})
    # .mappings() convierte cada fila en un dict usable
    filas = result.mappings().all()
    return [ dict(row) for row in filas ]

def obtener_productos_sucursal(sucursal_id, busqueda=None):
    """
    Llama a sp_GetProductosPorSucursal y opcionalmente filtra por nombre.
    """
    sql = text("EXEC sp_GetProductosPorSucursal :sucursal_id")
    resultado = db.session.execute(sql, {'sucursal_id': sucursal_id})
    productos = [
        {
            'producto_sucursal_id': row['producto_sucursal_id'],
            'producto_id':           row['producto_id'],
            'producto':              row['producto'],
            'stock_actual':          row['stock_actual'],
            'stock_minimo':          row['stock_minimo']
        }
        for row in resultado
    ]

    if busqueda:
        palabra = busqueda.strip().lower()
        productos = [p for p in productos if palabra in p['producto'].lower()]

    return productos


def obtener_todos_los_productos():
    """
    Consulta la vista vw_TodosLosProductos y retorna lista de diccionarios con:
    producto_sucursal_id, producto_id, producto, categoria, proveedor,
    sucursal_id, sucursal, stock_actual, stock_minimo
    """
    sql = text("SELECT * FROM vw_TodosLosProductos")
    resultado = db.session.execute(sql)
    return [dict(row) for row in resultado]
