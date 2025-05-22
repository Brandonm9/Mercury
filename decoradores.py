# decoradores.py
from functools import wraps
from flask import abort
from flask_login import current_user, login_required
import sys

def permiso_requerido(nombre_permiso):
    def decorator(func):
        @wraps(func)
        @login_required
        def wrapper(*args, **kwargs):
            permisos = [p.nombre for p in current_user.rol.permisos]
            # —— DEBUG: imprime comprobación de permiso ——
            print(f"[DEBUG permiso] Ruta: {func.__name__}", file=sys.stderr)
            print(f"[DEBUG permiso] Requiere: {nombre_permiso}", file=sys.stderr)
            print(f"[DEBUG permiso] Tiene: {permisos}", file=sys.stderr)
            # ————————————————————————————————
            if nombre_permiso not in permisos:
                abort(403)
            return func(*args, **kwargs)
        return wrapper
    return decorator
