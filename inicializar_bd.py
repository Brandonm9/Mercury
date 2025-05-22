# inicializar_bd.py

from app import app, db
import modelos
from modelos import Rol, Permiso, RolesPermisos

def main():
    # crear todas las tablas según los modelos
    with app.app_context():
        db.create_all()

        # datos iniciales: roles
        rol_empleado = Rol(nombre='empleado', descripcion='Puede registrar movimientos y consultar stock')
        rol_gerente  = Rol(nombre='gerente',  descripcion='Puede aprobar órdenes y generar reportes')
        rol_admin    = Rol(nombre='administrador', descripcion='Acceso completo al sistema')

        # datos iniciales: permisos
        p1 = Permiso(nombre='crear_producto',    descripcion='Alta de productos')
        p2 = Permiso(nombre='editar_producto',   descripcion='Modificación de productos')
        p3 = Permiso(nombre='ver_reportes',      descripcion='Acceso a reportes e indicadores')
        p4 = Permiso(nombre='gestionar_usuarios',descripcion='Crear/editar usuarios y roles')
        p5 = Permiso(nombre='ajustar_inventario',descripcion='Realizar ajustes masivos de stock')

        # agregar roles y permisos a la sesión
        db.session.add_all([rol_empleado, rol_gerente, rol_admin, p1, p2, p3, p4, p5])
        db.session.commit()

        # asignar permisos a roles
        # empleado: solo crear_producto, editar_producto, ajustar_inventario
        rol_empleado.permisos.extend([p1, p2])
        # gerente: p1, p2, p3, p5
        rol_gerente.permisos.extend([p1, p2, p3, p5])
        # administrador: todos
        rol_admin.permisos.extend([p1, p2, p3, p4, p5])

        db.session.commit()
        print("Tablas creadas y datos iniciales insertados correctamente")

if __name__ == "__main__":
    main()