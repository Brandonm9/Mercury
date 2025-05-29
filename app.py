# app.py
from flask import Flask, redirect, url_for
from flask_bcrypt import Bcrypt
from configuracion import Configuración
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user

# Inicializar extensiones (sin aplicación)
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuración)

    # Inicializar extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)  
    login_manager.login_view = 'autenticacion.login'

    # Registrar blueprints
    from autenticacion import autenticacion as bp_autenticacion
    from empleados import empleados as bp_empleados
    from gerentes import gerentes as bp_gerentes
    from administrador import administrador as bp_administrador

    app.register_blueprint(bp_autenticacion)
    app.register_blueprint(bp_empleados, url_prefix='/empleados')
    app.register_blueprint(bp_gerentes, url_prefix='/gerentes')
    app.register_blueprint(bp_administrador, url_prefix='/administrador')

    # Ruta raíz que redirige al login o panel según rol
    @app.route('/')
    def raiz():
        if current_user.is_authenticated:
            rol = current_user.rol
            if rol == 'Empleado':
                return redirect(url_for('empleados.panel'))
            if rol == 'Gerente':
                return redirect(url_for('gerentes.panel'))
            if rol == 'Administrador':
                return redirect(url_for('administrador.panel_administrador'))
        return redirect(url_for('autenticacion.login'))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

