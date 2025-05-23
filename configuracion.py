# configuracion.py
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Configuración:
    CLAVE_SECRETA = os.getenv('CLAVE_SECRETA', 'clave_por_defecto')
    SECRET_KEY = CLAVE_SECRETA  # ← esta línea es la que hace falta

    SERVIDOR = os.getenv('BD_HOST', 'localhost')
    PUERTO = os.getenv('BD_PUERTO', '1433')
    USUARIO_BD = os.getenv('BD_USUARIO', 'SA')
    CLAVE_BD = os.getenv('BD_CLAVE', '')
    NOMBRE_BD = os.getenv('BD_NOMBRE', 'InventarioDB')

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{USUARIO_BD}:{CLAVE_BD}"
        f"@{SERVIDOR},{PUERTO}/{NOMBRE_BD}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
