# modelos.py
from app import db
from flask_login import UserMixin

# tabla roles
class Rol(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.String(200))
    permisos = db.relationship('Permiso', secondary='roles_permisos', backref=db.backref('roles', lazy='dynamic'))

# tabla permisos
class Permiso(db.Model):
    __tablename__ = 'permisos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.String(200))

# tabla intermedia roles_permisos
class RolesPermisos(db.Model):
    __tablename__ = 'roles_permisos'
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)
    permiso_id = db.Column(db.Integer, db.ForeignKey('permisos.id'), primary_key=True)

# tabla usuarios
class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(255), unique=True, nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.getdate(), nullable=False)
    es_activo = db.Column(db.Boolean, default=True, nullable=False)
    rol = db.relationship('Rol', backref='usuarios')

# tabla categorias
class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    descripcion = db.Column(db.Text)

# tabla proveedores
class Proveedor(db.Model):
    __tablename__ = 'proveedores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15))
    direccion = db.Column(db.String(200))
    correo = db.Column(db.String(100))
    ruc_nit = db.Column(db.String(20), unique=True, nullable=False)

# tabla sucursales
class Sucursal(db.Model):
    __tablename__ = 'sucursales'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200))
    productos = db.relationship('Producto', backref='sucursal', lazy='dynamic')
    movimientos = db.relationship('Movimiento', backref='sucursal', lazy='dynamic')

# tabla productos
class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    precio_compra = db.Column(db.Numeric(10,2))
    precio_venta = db.Column(db.Numeric(10,2))
    stock_actual = db.Column(db.Integer, default=0, nullable=False)
    stock_minimo = db.Column(db.Integer, default=0, nullable=False)
    fecha_caducidad = db.Column(db.Date)
    codigo_de_barras = db.Column(db.String(50), unique=True, nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedores.id'), nullable=False)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'), nullable=False)
    movimientos = db.relationship('Movimiento', backref='producto', lazy='dynamic')
    alertas = db.relationship('Alerta', backref='producto', lazy='dynamic')

# tabla movimientos
class Movimiento(db.Model):
    __tablename__ = 'movimientos'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, default=db.func.getdate(), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    motivo = db.Column(db.Text)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('sucursales.id'), nullable=False)
    usuario = db.relationship('Usuario', backref='movimientos')

# tabla alertas
class Alerta(db.Model):
    __tablename__ = 'alertas'
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    fecha_generada = db.Column(db.DateTime, default=db.func.getdate(), nullable=False)
    leida = db.Column(db.Boolean, default=False, nullable=False)

# tabla auditoria
class Auditoria(db.Model):
    __tablename__ = 'auditoria'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    accion = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, default=db.func.getdate(), nullable=False)
    tabla_afectada = db.Column(db.String(50), nullable=False)
    usuario = db.relationship('Usuario', backref='auditorias')
