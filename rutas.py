# rutas.py
from flask import request, jsonify, render_template, redirect, url_for
from flask_login import login_required, current_user
from app import app, db
from modelos import Producto, Movimiento
from decoradores import permiso_requerido
from sqlalchemy import func

# ——— API JSON ———

@app.route("/productos", methods=["GET"])
@login_required
@permiso_requerido("productos.ver")
def listar_productos():
    productos = Producto.query.all()
    resultado = [
        {
            "id": p.id,
            "nombre": p.nombre,
            "precio_venta": float(p.precio_venta or 0),
            "stock_actual": p.stock_actual
        } for p in productos
    ]
    return jsonify(resultado), 200

@app.route("/productos/<int:id>", methods=["GET"])
@login_required
@permiso_requerido("productos.ver")
def obtener_producto(id):
    p = Producto.query.get_or_404(id)
    return jsonify({
        "id": p.id,
        "nombre": p.nombre,
        "descripcion": p.descripcion,
        "precio_compra": float(p.precio_compra or 0),
        "precio_venta": float(p.precio_venta or 0),
        "stock_actual": p.stock_actual,
        "stock_minimo": p.stock_minimo,
        "fecha_caducidad": p.fecha_caducidad.isoformat() if p.fecha_caducidad else None,
        "codigo_de_barras": p.codigo_de_barras
    }), 200

@app.route("/productos", methods=["POST"])
@login_required
@permiso_requerido("productos.crear")
def crear_producto():
    datos = request.get_json()
    p = Producto(
        nombre=datos.get("nombre"),
        descripcion=datos.get("descripcion"),
        categoria_id=datos.get("categoria_id"),
        precio_compra=datos.get("precio_compra"),
        precio_venta=datos.get("precio_venta"),
        stock_actual=datos.get("stock_actual", 0),
        stock_minimo=datos.get("stock_minimo", 0),
        fecha_caducidad=datos.get("fecha_caducidad"),
        codigo_de_barras=datos.get("codigo_de_barras"),
        proveedor_id=datos.get("proveedor_id"),
        sucursal_id=datos.get("sucursal_id")
    )
    db.session.add(p)
    db.session.commit()
    return jsonify({"mensaje": "Producto creado", "id": p.id}), 201

@app.route("/productos/<int:id>", methods=["PUT"])
@login_required
@permiso_requerido("productos.editar")
def actualizar_producto(id):
    p = Producto.query.get_or_404(id)
    datos = request.get_json()
    for campo in ["nombre","descripcion","precio_compra","precio_venta",
                  "stock_actual","stock_minimo","fecha_caducidad",
                  "codigo_de_barras","categoria_id","proveedor_id","sucursal_id"]:
        if campo in datos:
            setattr(p, campo, datos[campo])
    db.session.commit()
    return jsonify({"mensaje": "Producto actualizado"}), 200

@app.route("/productos/<int:id>", methods=["DELETE"])
@login_required
@permiso_requerido("productos.eliminar")
def borrar_producto(id):
    p = Producto.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({"mensaje": "Producto eliminado"}), 200

# ——— INTERFAZ WEB PRODUCTOS ———

@app.route("/productos/html")
@login_required
@permiso_requerido("productos.ver")
def listar_productos_html():
    productos = Producto.query.all()
    return render_template("productos_listar.html", productos=productos)

@app.route("/productos/nuevo", methods=["GET", "POST"])
@login_required
@permiso_requerido("productos.crear")
def nuevo_producto():
    if request.method == "POST":
        datos = request.form
        p = Producto(
            nombre=datos["nombre"],
            descripcion=datos.get("descripcion",""),
            categoria_id=datos.get("categoria_id", None),
            precio_compra=datos.get("precio_compra", 0),
            precio_venta=datos.get("precio_venta", 0),
            stock_actual=datos.get("stock_actual", 0),
            stock_minimo=datos.get("stock_minimo", 0),
            fecha_caducidad=datos.get("fecha_caducidad", None),
            codigo_de_barras=datos["codigo_de_barras"],
            proveedor_id=datos.get("proveedor_id", None),
            sucursal_id=datos.get("sucursal_id", None)
        )
        db.session.add(p)
        db.session.commit()
        return redirect(url_for("listar_productos_html"))
    return render_template("producto_form.html", producto=None)

@app.route("/productos/editar/<int:id>", methods=["GET", "POST"])
@login_required
@permiso_requerido("productos.editar")
def editar_producto_html(id):
    p = Producto.query.get_or_404(id)
    if request.method == "POST":
        datos = request.form
        p.nombre           = datos["nombre"]
        p.descripcion      = datos.get("descripcion", p.descripcion)
        p.categoria_id     = datos.get("categoria_id", p.categoria_id)
        p.precio_compra    = datos.get("precio_compra", p.precio_compra)
        p.precio_venta     = datos.get("precio_venta", p.precio_venta)
        p.stock_actual     = datos.get("stock_actual", p.stock_actual)
        p.stock_minimo     = datos.get("stock_minimo", p.stock_minimo)
        p.fecha_caducidad  = datos.get("fecha_caducidad", p.fecha_caducidad)
        p.codigo_de_barras = datos["codigo_de_barras"]
        p.proveedor_id     = datos.get("proveedor_id", p.proveedor_id)
        p.sucursal_id      = datos.get("sucursal_id", p.sucursal_id)
        db.session.commit()
        return redirect(url_for("listar_productos_html"))
    return render_template("producto_form.html", producto=p)

@app.route("/productos/borrar/<int:id>")
@login_required
@permiso_requerido("productos.eliminar")
def borrar_producto_html(id):
    p = Producto.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for("listar_productos_html"))

# ——— INTERFAZ EMPLEADO ———

@app.route("/empleado/inventario")
@login_required
@permiso_requerido("ajustar_inventario")
def inventario_empleado():
    productos = Producto.query.all()
    return render_template("inventario_empleado.html", productos=productos)

@app.route("/empleado/movimiento/nuevo/<int:producto_id>", methods=["GET","POST"])
@login_required
@permiso_requerido("ajustar_inventario")
def movimiento_empleado(producto_id):
    p = Producto.query.get_or_404(producto_id)
    tipo = request.args.get("tipo", "entrada")
    if request.method == "POST":
        datos = request.form
        cantidad = int(datos["cantidad"])
        motivo    = datos.get("motivo", "")
        mov = Movimiento(
            tipo=tipo,
            cantidad=cantidad,
            usuario_id=current_user.id,
            producto_id=producto_id,
            motivo=motivo,
            sucursal_id=p.sucursal_id
        )
        if tipo == "entrada":
            p.stock_actual += cantidad
        else:
            p.stock_actual = max(0, p.stock_actual - cantidad)
        db.session.add(mov)
        db.session.commit()
        return redirect(url_for("inventario_empleado"))
    return render_template("movimiento_form.html", producto=p, tipo=tipo)

# ——— INTERFAZ GERENTE ———

@app.route("/gerente/dashboard")
@login_required
@permiso_requerido("reportes.ver")
def dashboard():
    ventas_mes = (
        db.session.query(
            func.month(Movimiento.fecha).label('mes'),
            func.sum(Movimiento.cantidad).label('total')
        )
        .filter(Movimiento.tipo == 'salida')
        .group_by(func.month(Movimiento.fecha))
        .all()
    )
    return render_template("dashboard.html", ventas_mes=ventas_mes)

#Generar reporte de ventas
from flask import Response
import pandas as pd
from io import BytesIO

@app.route("/gerente/reportes/ventas.xlsx")
@login_required
@permiso_requerido("reportes.ver")
def reporte_ventas_excel():
    ventas = (
        db.session.query(
            func.month(Movimiento.fecha).label('mes'),
            func.sum(Movimiento.cantidad).label('total')
        )
        .filter(Movimiento.tipo == 'salida')
        .group_by(func.month(Movimiento.fecha))
        .all()
    )
    df = pd.DataFrame(ventas, columns=['Mes', 'Total Vendido'])

    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Ventas')
    output.seek(0)

    return Response(
        output.read(),
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={'Content-Disposition': 'attachment; filename=ventas.xlsx'}
    )

