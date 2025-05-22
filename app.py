# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from configuracion import Config
from flask_login import LoginManager

load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

from modelos import Usuario  # <–– aquí, tras db y login_manager

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# ahora importa el resto
import modelos
import autenticacion
import rutas

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


