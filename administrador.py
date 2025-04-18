# administrador.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user
from autenticacion import rol_requerido
from servicios import (
    obtener_sucursales,
    ventas_por_sucursal,
    ventas_por_vendedor,
    obtener_auditoria,
    obtener_todos_los_productos_para_admin
)
from modelos import Auditoria
from app import db

administrador = Blueprint(
    'administrador',
    __name__,
    template_folder='templates/administrador',
    url_prefix='/administrador'
)

@administrador.route('/', methods=['GET'])
@rol_requerido(['Administrador'])
def panel_administrador():
    sucursales = obtener_sucursales()
    id_sucursal = request.args.get('sucursal_id', type=int)

    ventas_suc = []
    ventas_vend = []
    
    if id_sucursal:
        ventas_suc = ventas_por_sucursal(id_sucursal)
        ventas_vend = ventas_por_vendedor(id_sucursal)

    auditorias = obtener_auditoria(id_sucursal)

    return render_template(
        'panel_administrador.html',
        sucursales=sucursales,
        ventas_suc=ventas_suc,
        ventas_vend=ventas_vend,
        auditorias=auditorias,
        id_sucursal=id_sucursal
    )

@administrador.route('/inventario', methods=['GET'])
@rol_requerido(['Administrador'])
def inventario_global():
    productos = obtener_todos_los_productos_para_admin()
    return render_template('inventario_global.html', productos=productos)


@administrador.route('/auditoria', methods=['GET'])
@rol_requerido(['Administrador'])
def auditoria():
    logs = obtener_auditoria()
    return render_template('auditoria.html', logs=logs)

@administrador.route('/auditoria/crear', methods=['POST'])
@rol_requerido(['Administrador'])
def crear_auditoria():
    accion = request.form.get('accion', '').strip()
    tabla  = request.form.get('tabla_afectada', '').strip()
    suc_id = request.form.get('sucursal_id', type=int)

    # Validaciones
    if not accion:
        flash('Debe indicar una descripción de la acción.', 'warning')
        return redirect(url_for('administrador.panel_administrador', sucursal_id=suc_id))
    if not tabla:
        flash('Debe seleccionar la tabla afectada.', 'warning')
        return redirect(url_for('administrador.panel_administrador', sucursal_id=suc_id))

    # Crear y guardar
    nueva = Auditoria(
        usuario_id=current_user.id,
        accion=accion,
        tabla_afectada=tabla
    )
    db.session.add(nueva)
    db.session.commit()
    flash('Nuevo registro de auditoría creado.', 'success')
    return redirect(url_for('administrador.panel_administrador', sucursal_id=suc_id))

@administrador.route('/sucursal/<int:id_sucursal>')
@rol_requerido(['Administrador'])
def ver_sucursal(id_sucursal):
    # Datos de ventas para gráficas de la sucursal
    datos = ventas_por_sucursal(id_sucursal)
    sucursal = Sucursal.query.get_or_404(id_sucursal)
    return render_template(
    'ventas_sucursal.html',
    sucursales=sucursales,
    selected_sucursal=selected,
    datos=datos,ventas_vendedores=ventas_vendedores)

@administrador.route('/api/ventas_sucursal')
@rol_requerido(['Administrador'])
def api_ventas_sucursal():
    # Endpoint JSON para gráficos
    id_sucursal = request.args.get('sucursal_id', type=int)
    datos = ventas_por_sucursal(id_sucursal)
    return jsonify(datos)
