# gerentes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import current_user
from autenticacion import rol_requerido
from servicios import (
    obtener_alertas_stock,
    ventas_por_sucursal,
    ventas_por_vendedor
)

gerentes = Blueprint('gerentes', __name__, template_folder='templates/gerentes')

@gerentes.route('/', methods=['GET'])
@rol_requerido(['Gerente'])
def panel():
    alertas = obtener_alertas_stock(current_user.sucursal_id)
    ventas   = ventas_por_sucursal(current_user.sucursal_id)
    menu_items = [
        {'texto': 'Panel Principal',     'endpoint': 'gerentes.panel'},
        {'texto': 'Ventas por vendedor', 'endpoint': 'gerentes.ventas_vendedor'},
        {'texto': 'Generar documento',   'endpoint': 'gerentes.documento_ventas'},
        {'texto': 'Hacer pedido',        'endpoint': 'gerentes.hacer_pedido'}
    ]
    return render_template(
        'panel_gerentes.html',
        alertas=alertas,
        ventas=ventas,
        menu_items=menu_items
    )

@gerentes.route('/ventas_vendedor', methods=['GET'])
@rol_requerido(['Gerente'])
def ventas_vendedor():
    alertas = obtener_alertas_stock(current_user.sucursal_id)
    ventas   = ventas_por_vendedor(current_user.sucursal_id)
    menu_items = [
        {'texto': 'Panel Principal',     'endpoint': 'gerentes.panel'},
        {'texto': 'Ventas por vendedor', 'endpoint': 'gerentes.ventas_vendedor'},
        {'texto': 'Generar documento',   'endpoint': 'gerentes.documento_ventas'},
        {'texto': 'Hacer pedido',        'endpoint': 'gerentes.hacer_pedido'}
    ]
    return render_template(
        'ventas_vendedor.html',
        alertas=alertas,
        ventas=ventas,
        menu_items=menu_items
    )

@gerentes.route('/documento_ventas', methods=['GET', 'POST'])
@rol_requerido(['Gerente'])
def documento_ventas():
    alertas = obtener_alertas_stock(current_user.sucursal_id)
    menu_items = [
        {'texto': 'Panel Principal',     'endpoint': 'gerentes.panel'},
        {'texto': 'Ventas por vendedor', 'endpoint': 'gerentes.ventas_vendedor'},
        {'texto': 'Generar documento',   'endpoint': 'gerentes.documento_ventas'},
        {'texto': 'Hacer pedido',        'endpoint': 'gerentes.hacer_pedido'}
    ]
    # Aquí podrías generar un doc (PDF, Excel, etc.)
    return render_template(
        'documento_ventas.html',
        alertas=alertas,
        menu_items=menu_items
    )

@gerentes.route('/hacer_pedido', methods=['POST'])
@rol_requerido(['Gerente'])
def hacer_pedido():
    # Sólo mostramos un flash; no hay lógica de envíos real
    flash('Pedido enviado al proveedor.', 'info')
    return redirect(url_for('gerentes.ventas_vendedor'))
