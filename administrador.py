from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user
from autenticacion import rol_requerido
from servicios import ventas_por_sucursal, obtener_todos_los_productos
from modelos import Sucursal

administrador = Blueprint('administrador', __name__, template_folder='templates/administrador')

@administrador.route('/')
@rol_requerido(['Administrador'])
def panel_administrador():
    # Lista todas las sucursales para mostrar en el menú
    sucursales = Sucursal.query.all()
    menu_items = [
        {'texto': 'Inventario Global', 'endpoint': 'administrador.inventario_global'}
    ] + [
        {
            'texto': suc.nombre,
            'endpoint': 'administrador.ver_sucursal',
            'args': {'id_sucursal': suc.id}
        }
        for suc in sucursales
    ]
    return render_template(
        'panel_administrador.html',
        sucursales=sucursales,
        menu_items=menu_items
    )

@administrador.route('/inventario')
@rol_requerido(['Administrador'])
def inventario_global():
    # Inventario completo desde la vista vw_TodosLosProductos
    productos = obtener_todos_los_productos()
    return render_template('inventario_global.html', productos=productos)

@administrador.route('/sucursal/<int:id_sucursal>')
@rol_requerido(['Administrador'])
def ver_sucursal(id_sucursal):
    # Datos de ventas para gráficas de la sucursal
    datos = ventas_por_sucursal(id_sucursal)
    sucursal = Sucursal.query.get_or_404(id_sucursal)
    return render_template('ventas_sucursal.html', datos=datos, sucursal=sucursal)

@administrador.route('/api/ventas_sucursal')
@rol_requerido(['Administrador'])
def api_ventas_sucursal():
    # Endpoint JSON para gráficos
    id_sucursal = request.args.get('sucursal_id', type=int)
    datos = ventas_por_sucursal(id_sucursal)
    return jsonify(datos)
