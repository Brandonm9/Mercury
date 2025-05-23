# app.py
from flask import Flask
from configuracion import Configuración
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Inicializar extensiones (sin aplicación)
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    """
    Factory de aplicación para evitar importaciones circulares.
    """
    app = Flask(__name__)
    app.config.from_object(Configuración)

    # Inicializar extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'autenticacion.login'

    # Registrar blueprints
    from autenticacion import autenticacion as bp_autenticacion
    from empleados import empleados as bp_empleados
    from gerentes import gerentes as bp_gerentes
    from administrador import administrador as bp_administrador

    app.register_blueprint(bp_autenticacion)
    app.register_blueprint(bp_empleados,   url_prefix='/empleados')
    app.register_blueprint(bp_gerentes,    url_prefix='/gerentes')
    app.register_blueprint(bp_administrador, url_prefix='/administrador')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
