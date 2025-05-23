# administrador.py
from flask import Blueprint, render_template, request, jsonify
from flask_login import current_user
from autenticacion import rol_requerido
from servicios import ventas_por_sucursal
from modelos import Sucursal

administrador = Blueprint('administrador', __name__, template_folder='templates/administrador')

@administrador.route('/administrador')
@rol_requerido(['Administrador'])
def panel_administrador():
    # Listar todas las sucursales
    sucursales = Sucursal.query.all()
    return render_template('panel_administrador.html', sucursales=sucursales)

@administrador.route('/administrador/sucursal/<int:id_sucursal>')
@rol_requerido(['Administrador'])
def ver_sucursal(id_sucursal):
    # JSON para gráficas de la sucursal seleccionada
    datos = ventas_por_sucursal(id_sucursal)
    sucursal = Sucursal.query.get_or_404(id_sucursal)
    return render_template('ventas_sucursal.html', datos=datos, sucursal=sucursal)

@administrador.route('/administrador/api/ventas_sucursal')
@rol_requerido(['Administrador'])
def api_ventas_sucursal():
    id_sucursal = request.args.get('sucursal_id', type=int)
    datos = ventas_por_sucursal(id_sucursal)
    return jsonify(datos)
