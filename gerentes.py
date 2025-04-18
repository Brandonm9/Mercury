# gerentes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request, send_file
from flask_login import current_user
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

from autenticacion import rol_requerido
from servicios import (
    obtener_alertas_stock,
    ventas_por_sucursal,
    ventas_por_vendedor,
    ventas_por_fecha
)

gerentes = Blueprint('gerentes', __name__, template_folder='templates/gerentes')

@gerentes.route('/', methods=['GET'])
@rol_requerido(['Gerente'])
def panel():
    alertas = obtener_alertas_stock(current_user.sucursal_id)
    ventas = ventas_por_sucursal(current_user.sucursal_id)
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

@gerentes.route('/documento_ventas', methods=['GET'])
@rol_requerido(['Gerente'])
def documento_ventas():
    alertas = obtener_alertas_stock(current_user.sucursal_id)
    menu_items = [
        {'texto': 'Panel Principal',     'endpoint': 'gerentes.panel'},
        {'texto': 'Ventas por vendedor', 'endpoint': 'gerentes.ventas_vendedor'},
        {'texto': 'Generar documento',   'endpoint': 'gerentes.documento_ventas'},
        {'texto': 'Hacer pedido',        'endpoint': 'gerentes.hacer_pedido'}
    ]
    return render_template(
        'documento_ventas.html',
        alertas=alertas,
        menu_items=menu_items
    )

@gerentes.route('/descargar_pdf', methods=['POST'])
@rol_requerido(['Gerente'])
def descargar_pdf():
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    if not start_date or not end_date:
        flash('Debes seleccionar ambas fechas.', 'warning')
        return redirect(url_for('gerentes.documento_ventas'))

    try:
        fecha_inicio = datetime.strptime(start_date, "%Y-%m-%d")
        fecha_fin = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        flash("Formato de fecha inválido.", "danger")
        return redirect(url_for('gerentes.documento_ventas'))

    ventas = ventas_por_fecha(current_user.sucursal_id, start_date, end_date)

    # Generar PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica", 12)
    p.drawString(40, 770, f"Reporte de ventas: {start_date} a {end_date}")
    y = 740
    p.drawString(40, y, "Fecha       Cantidad")
    y -= 20
    for v in ventas:
        p.drawString(40, y, f"{v['fecha']}    {v['total']}")
        y -= 20
        if y < 50:
            p.showPage()
            y = 770
    p.save()
    buffer.seek(0)

    nombre_pdf = f"reporte_ventas_{start_date}_a_{end_date}.pdf"
    return send_file(
        buffer,
        as_attachment=True,
        download_name=nombre_pdf,
        mimetype='application/pdf'
    )

@gerentes.route('/ventas_vendedor', methods=['GET'])
@rol_requerido(['Gerente'])
def ventas_vendedor():
    alertas = obtener_alertas_stock(current_user.sucursal_id)
    ventas = ventas_por_vendedor(current_user.sucursal_id)
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

@gerentes.route('/hacer_pedido', methods=['POST'])
@rol_requerido(['Gerente'])
def hacer_pedido():
    flash('Pedido enviado al proveedor.', 'info')
    return redirect(url_for('gerentes.ventas_vendedor'))
