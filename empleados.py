# empleados.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user
from app import db
from modelos import ProductoSucursal, Movimiento
from autenticacion import rol_requerido
from servicios import obtener_alertas_stock, obtener_productos_sucursal  # :contentReference[oaicite:0]{index=0}

empleados = Blueprint('empleados', __name__, template_folder='templates/empleados')

@empleados.route('/empleados')
@rol_requerido(['Empleado'])
def panel():
    alertas   = obtener_alertas_stock(current_user.sucursal_id)
    productos = obtener_productos_sucursal(current_user.sucursal_id)  # traemos todos
    menu_items = [
        {'texto':'Inventario',        'endpoint':'empleados.inventario'},
        {'texto':'Registrar Entrada', 'endpoint':'empleados.ingresar_producto'},
        {'texto':'Registrar Venta',   'endpoint':'empleados.registrar_venta'},
        {'texto':'Ajustar Stock',     'endpoint':'empleados.ajustar_stock'},
    ]
    return render_template(
        'panel_empleados.html',
        alertas=alertas,
        productos=productos,
        menu_items=menu_items
    )

@empleados.route('/empleados/editar_stock_directo', methods=['POST'])
@rol_requerido(['Empleado'])
def editar_stock_directo():
    # Ajusta stock SIN crear un Movimiento
    ps_id = request.form.get('producto_sucursal_id', type=int)
    nuevo = request.form.get('nuevo_stock', type=int)
    ps    = ProductoSucursal.query.get_or_404(ps_id)
    ps.stock_actual = nuevo
    db.session.commit()
    flash(f"Stock de “{ps.producto.nombre}” ajustado a {nuevo}.", 'success')
    return redirect(url_for('empleados.panel'))

@empleados.route('/empleados/inventario')
@rol_requerido(['Empleado'])
def inventario():
    busqueda = request.args.get('q', '', type=str)
    productos = obtener_productos_sucursal(current_user.sucursal_id, busqueda)
    menu_items = [
        {'texto':'Inventario',        'endpoint':'empleados.inventario'},
        {'texto':'Registrar Entrada', 'endpoint':'empleados.ingresar_producto'},
        {'texto':'Registrar Venta',   'endpoint':'empleados.registrar_venta'},
        {'texto':'Ajustar Stock',     'endpoint':'empleados.ajustar_stock'},
    ]
    return render_template(
        'productos_empleados.html',
        productos=productos,
        busqueda=busqueda,
        menu_items=menu_items
    )

@empleados.route('/empleados/ingresar_producto', methods=['GET', 'POST'])
@rol_requerido(['Empleado'])
def ingresar_producto():
    if request.method == 'POST':
        producto_sucursal_id = request.form.get('producto_sucursal_id')
        cantidad             = int(request.form.get('cantidad'))
        motivo               = request.form.get('motivo')

        movimiento = Movimiento(
            tipo='entrada', cantidad=cantidad,
            usuario_id=current_user.id,
            producto_sucursal_id=producto_sucursal_id,
            motivo=motivo
        )
        db.session.add(movimiento)
        ps = ProductoSucursal.query.get(producto_sucursal_id)
        ps.stock_actual += cantidad
        db.session.commit()
        flash('Entrada de producto registrada.', 'success')
        return redirect(url_for('empleados.panel'))
    productos = ProductoSucursal.query.filter_by(sucursal_id=current_user.sucursal_id).all()
    return render_template('ingresar_producto.html', productos=productos)

@empleados.route('/empleados/registrar_venta', methods=['GET', 'POST'])
@rol_requerido(['Empleado'])
def registrar_venta():
    if request.method == 'POST':
        producto_sucursal_id = request.form.get('producto_sucursal_id')
        cantidad             = int(request.form.get('cantidad'))
        motivo               = request.form.get('motivo')

        movimiento = Movimiento(
            tipo='salida', cantidad=cantidad,
            usuario_id=current_user.id,
            producto_sucursal_id=producto_sucursal_id,
            motivo=motivo
        )
        db.session.add(movimiento)
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
        nuevo_stock          = int(request.form.get('nuevo_stock'))
        motivo               = request.form.get('motivo')

        ps        = ProductoSucursal.query.get(producto_sucursal_id)
        diferencia= nuevo_stock - ps.stock_actual
        tipo      = 'entrada' if diferencia > 0 else 'salida'
        movimiento= Movimiento(
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
