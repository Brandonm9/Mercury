# autenticacion.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db, login_manager
from modelos import Usuario
#from flask_bcrypt import generate_password_hash, check_password_hash

autenticacion = Blueprint('autenticacion', __name__, template_folder='templates/autenticacion')

@login_manager.user_loader
def cargar_usuario(id):
    return Usuario.query.get(int(id))

@autenticacion.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        contrasena = request.form.get('contrasena')
        usuario = Usuario.query.filter_by(correo=correo).first()

        print(f"[DEBUG] login intento: correo={correo}, usuario_encontrado={bool(usuario)}")
        print(f"[DEBUG] hash en BD para {correo}: {usuario.contrasena}")
        print(f"[DEBUG] resultado check: {usuario.verificar_contrasena(contrasena)}")

        if usuario and usuario.verificar_contrasena(contrasena):
            login_user(usuario)
            flash('Inicio de sesión correcto.', 'success')

        
            # Redirigir al panel correcto según el rol
            if usuario.rol == 'Empleado':
                return redirect(url_for('empleados.panel'))
            elif usuario.rol == 'Gerente':
                return redirect(url_for('gerentes.panel'))
            elif usuario.rol == 'Administrador':
                return redirect(url_for('administrador.panel_administrador'))
        else:
            flash('Credenciales incorrectas.', 'danger')

    return render_template('login.html')


@autenticacion.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('autenticacion.login'))

# Decorador de autorización por roles
def rol_requerido(roles_permitidos):
    def decorador(func):
        @login_required
        def envoltura(*args, **kwargs):
            if current_user.rol not in roles_permitidos:
                flash('No tienes permiso para acceder a esta página.', 'warning')
                return redirect(url_for('autenticacion.login'))
            return func(*args, **kwargs)
        envoltura.__name__ = func.__name__
        return envoltura
    return decorador

# Ejemplo de uso en otros blueprints:
# @autenticacion.route('/ruta_empleado')
# @rol_requerido(['Empleado'])
# def panel_empleado():
#     ...
