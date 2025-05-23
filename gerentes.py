# gerentes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import current_user
from app import db
from modelos import Movimiento, Usuario
from autenticacion import rol_requerido
from servicios import obtener_alertas_stock, ventas_por_sucursal, ventas_por_vendedor

gerentes = Blueprint('gerentes', __name__, template_folder='templates/gerentes')

@gerentes.route('/gerentes')
@rol_requerido(['Gerente'])
def panel():
    # Alertas de stock bajo para la sucursal del gerente
    alertas = obtener_alertas_stock(current_user.sucursal_id)
    return render_template('panel_gerentes.html', alertas=alertas)

@gerentes.route('/gerentes/api/ventas')
@rol_requerido(['Gerente'])
def api_ventas():
    # Devuelve datos de ventas por fecha para gráficas
    datos = ventas_por_sucursal(current_user.sucursal_id)
    return jsonify(datos)

@gerentes.route('/gerentes/ventas_por_vendedor')
@rol_requerido(['Gerente'])
def ventas_vendedor():
    # Tabla de totales por vendedor
    tabla = ventas_por_vendedor(current_user.sucursal_id)
    return render_template('ventas_vendedor.html', tabla=tabla)

@gerentes.route('/gerentes/documento_ventas', methods=['GET', 'POST'])
@rol_requerido(['Gerente'])
def documento_ventas():
    if request.method == 'POST':
        fecha = request.form.get('fecha')  # formato YYYY-MM-DD
        # Generar PDF de ventas en esa fecha (stub)
        # Aquí integrar ReportLab o WeasyPrint
        flash(f'Documento de ventas para {fecha} generado.', 'success')
        return redirect(url_for('gerentes.panel'))
    return render_template('documento_ventas.html')

@gerentes.route('/gerentes/hacer_pedido', methods=['POST'])
@rol_requerido(['Gerente'])
def hacer_pedido():
    # Botón que simula pedido al proveedor
    flash('Pedido al proveedor realizado correctamente.', 'info')
    return redirect(url_for('gerentes.panel'))
