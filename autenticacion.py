# autenticacion.py
from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from app import app, db
from modelos import Usuario
from decoradores import permiso_requerido


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("listar_productos_html"))

    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = Usuario.query.filter_by(username=username).first()

        if user and user.es_activo and check_password_hash(user.password_hash, password):
            # DEBUG
            import sys
            print(f"[DEBUG login] Usuario: {user.username}", file=sys.stderr)
            print(f"[DEBUG login] Rol: {user.rol.nombre}", file=sys.stderr)
            print(f"[DEBUG login] Permisos: {[p.nombre for p in user.rol.permisos]}", file=sys.stderr)

            login_user(user)
            next_page = request.args.get("next") or url_for("listar_productos_html")
            return redirect(next_page)

        error = "Usuario o contraseña inválidos"

    return render_template("login.html", error=error)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

