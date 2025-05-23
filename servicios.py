# servicios.py
from app import db
from modelos import ProductoSucursal, Movimiento, Usuario
from sqlalchemy import func, cast, Date


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
    Retorna ventas totales por vendedor en una sucursal.
    Devuelve lista de tuplas: [(nombre_vendedor, total_ventas), ...]
    """
    resultados = (
        db.session.query(
            Usuario.nombre.label('vendedor'),
            func.sum(Movimiento.cantidad).label('total')
        )
        .join(Movimiento, Movimiento.usuario_id == Usuario.id)
        .join(ProductoSucursal, Movimiento.producto_sucursal_id == ProductoSucursal.id)
        .filter(
            Movimiento.tipo == 'salida',
            Usuario.sucursal_id == sucursal_id
        )
        .group_by(Usuario.nombre)
        .order_by(Usuario.nombre)
        .all()
    )
    return resultados
