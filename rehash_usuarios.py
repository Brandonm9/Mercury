# rehash_usuarios.py
from app import create_app, db
from modelos import Usuario

app = create_app()
with app.app_context():
    usuarios = Usuario.query.all()
    for u in usuarios:
        if u.rol == 'Administrador':
            u.set_contrasena('admin123')   # admin
        else:
            u.set_contrasena('clave123')   # empleados y gerentes
    db.session.commit()
    print(f"✅ Rehashed {len(usuarios)} usuarios.")
