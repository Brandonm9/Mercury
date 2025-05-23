# empleados.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user
from app import db
from modelos import ProductoSucursal, Movimiento
from autenticacion import rol_requerido
from servicios import obtener_alertas_stock

empleados = Blueprint('empleados', __name__, template_folder='templates/empleados')

@empleados.route('/empleados')
@rol_requerido(['Empleado'])
def panel():
    # Mostrar alerta de productos con stock bajo
    alertas = obtener_alertas_stock(current_user.sucursal_id)
    return render_template('panel_empleados.html', alertas=alertas)

@empleados.route('/empleados/ingresar_producto', methods=['GET', 'POST'])
@rol_requerido(['Empleado'])
def ingresar_producto():
    if request.method == 'POST':
        sucursal_id = current_user.sucursal_id
        producto_sucursal_id = request.form.get('producto_sucursal_id')
        cantidad = int(request.form.get('cantidad'))
        motivo = request.form.get('motivo')

        movimiento = Movimiento(
            tipo='entrada', cantidad=cantidad,
            usuario_id=current_user.id,
            producto_sucursal_id=producto_sucursal_id,
            motivo=motivo
        )
        db.session.add(movimiento)
        # Actualizar stock
        ps = ProductoSucursal.query.get(producto_sucursal_id)
        ps.stock_actual += cantidad
        db.session.commit()
        flash('Entrada de producto registrada.', 'success')
        return redirect(url_for('empleados.panel'))
    # GET: mostrar formulario con lista de productos de la sucursal
    productos = ProductoSucursal.query.filter_by(sucursal_id=current_user.sucursal_id).all()
    return render_template('ingresar_producto.html', productos=productos)

@empleados.route('/empleados/registrar_venta', methods=['GET', 'POST'])
@rol_requerido(['Empleado'])
def registrar_venta():
    if request.method == 'POST':
        producto_sucursal_id = request.form.get('producto_sucursal_id')
        cantidad = int(request.form.get('cantidad'))
        motivo = request.form.get('motivo')

        movimiento = Movimiento(
            tipo='salida', cantidad=cantidad,
            usuario_id=current_user.id,
            producto_sucursal_id=producto_sucursal_id,
            motivo=motivo
        )
        db.session.add(movimiento)
        # Actualizar stock
        ps = ProductoSucursal.query.get(producto_sucursal_id)
        ps.stock_actual -= cantidad
        db.session.commit()
        flash('Venta registrada y stock actualizado.', 'success')
        return redirect(url_for('empleados.panel'))
    productos = ProductoSucursal.query.filter_by(sucursal_id=current_user.sucursal_id).all()
    return render_template('registrar_venta.html', productos=productos)

@empleados.route('/empleados/ajustar_stock', methods=['GET', 'POST'])
@rol_requerido(['Empleado'])
def ajustar_stock():
    if request.method == 'POST':
        producto_sucursal_id = request.form.get('producto_sucursal_id')
        nuevo_stock = int(request.form.get('nuevo_stock'))
        motivo = request.form.get('motivo')

        ps = ProductoSucursal.query.get(producto_sucursal_id)
        diferencia = nuevo_stock - ps.stock_actual
        tipo = 'entrada' if diferencia > 0 else 'salida'
        movimiento = Movimiento(
            tipo=tipo, cantidad=abs(diferencia),
            usuario_id=current_user.id,
            producto_sucursal_id=producto_sucursal_id,
            motivo=motivo
        )
        db.session.add(movimiento)
        ps.stock_actual = nuevo_stock
        db.session.commit()
        flash('Stock ajustado correctamente.', 'success')
        return redirect(url_for('empleados.panel'))
    productos = ProductoSucursal.query.filter_by(sucursal_id=current_user.sucursal_id).all()
    return render_template('ajustar_stock.html', productos=productos)

# servicios.py debe incluir:
# def obtener_alertas_stock(sucursal_id):
#     return ProductoSucursal.query.filter(
#         ProductoSucursal.sucursal_id == sucursal_id,
#         ProductoSucursal.stock_actual <= ProductoSucursal.stock_minimo
#     ).all()
