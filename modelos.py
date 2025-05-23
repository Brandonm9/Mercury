from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime


class Sucursal(db.Model):
    __tablename__ = 'Sucursal'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)

    usuarios = db.relationship('Usuario', back_populates='sucursal')
    productos_sucursal = db.relationship('ProductoSucursal', back_populates='sucursal')

    def __repr__(self):
        return f"<Sucursal {self.nombre}>"


class Categoria(db.Model):
    __tablename__ = 'Categoria'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text)

    productos = db.relationship('Producto', back_populates='categoria')

    def __repr__(self):
        return f"<Categoria {self.nombre}>"


class Proveedor(db.Model):
    __tablename__ = 'Proveedor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15))
    direccion = db.Column(db.String(200))
    correo = db.Column(db.String(100))
    ruc_nit = db.Column('RUC_NIT', db.String(20), unique=True)

    productos = db.relationship('Producto', back_populates='proveedor')

    def __repr__(self):
        return f"<Proveedor {self.nombre}>"


class Producto(db.Model):
    __tablename__ = 'Producto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('Categoria.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('Proveedor.id'), nullable=False)

    categoria = db.relationship('Categoria', back_populates='productos')
    proveedor = db.relationship('Proveedor', back_populates='productos')
    existencias = db.relationship('ProductoSucursal', back_populates='producto')

    def __repr__(self):
        return f"<Producto {self.nombre}>"


class ProductoSucursal(db.Model):
    __tablename__ = 'ProductoSucursal'
    id = db.Column(db.Integer, primary_key=True)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('Sucursal.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('Producto.id'), nullable=False)
    stock_actual = db.Column(db.Integer, nullable=False)
    stock_minimo = db.Column(db.Integer, nullable=False)

    sucursal = db.relationship('Sucursal', back_populates='productos_sucursal')
    producto = db.relationship('Producto', back_populates='existencias')
    movimientos = db.relationship('Movimiento', back_populates='producto_sucursal')

    __table_args__ = (
        db.UniqueConstraint('sucursal_id', 'producto_id', name='UC_SucursalProducto'),
    )

    def __repr__(self):
        return f"<Existencia {self.producto.nombre} en {self.sucursal.nombre}>"


class Usuario(UserMixin, db.Model):
    __tablename__ = 'Usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    contrasena = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    sucursal_id = db.Column(db.Integer, db.ForeignKey('Sucursal.id'))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.Boolean, default=True)

    sucursal = db.relationship('Sucursal', back_populates='usuarios')
    movimientos = db.relationship('Movimiento', back_populates='usuario')
    auditorias = db.relationship('Auditoria', back_populates='usuario')

    def __repr__(self):
        return f"<Usuario {self.nombre} ({self.rol})>"

    def verificar_contrasena(self, contrasena_plana):
        return self.contrasena == contrasena_plana



@login_manager.user_loader
def cargar_usuario(id):
    return Usuario.query.get(int(id))


class Movimiento(db.Model):
    __tablename__ = 'Movimiento'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(20), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=False)
    producto_sucursal_id = db.Column(db.Integer, db.ForeignKey('ProductoSucursal.id'), nullable=False)
    motivo = db.Column(db.String(255))

    usuario = db.relationship('Usuario', back_populates='movimientos')
    producto_sucursal = db.relationship('ProductoSucursal', back_populates='movimientos')

    def __repr__(self):
        return f"<Movimiento {self.tipo} {self.cantidad} unidad(es)>"


class Auditoria(db.Model):
    __tablename__ = 'Auditoria'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('Usuario.id'), nullable=False)
    accion = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    tabla_afectada = db.Column(db.String(50), nullable=False)

    usuario = db.relationship('Usuario', back_populates='auditorias')

    def __repr__(self):
        return f"<Auditoria {self.usuario.nombre} - {self.accion}>"
