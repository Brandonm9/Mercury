create database mercuryDB
go

use mercuryDB
go

-- roles de usuario
create table roles (
  id int identity(1,1) primary key,
  nombre varchar(50) not null unique,
  descripcion varchar(200)
)
go

-- permisos disponibles en el sistema
create table permisos (
  id int identity(1,1) primary key,
  nombre varchar(50) not null unique,
  descripcion varchar(200)
)
go

-- asignación de permisos a roles
create table roles_permisos (
  role_id int not null references roles(id),
  permiso_id int not null references permisos(id),
  primary key (role_id, permiso_id)
)
go

-- usuarios con rol y estado
create table usuarios (
  id int identity(1,1) primary key,
  nombre varchar(100) not null,
  correo varchar(255) not null unique,
  contrasena varchar(255) not null,
  rol_id int not null references roles(id),
  fecha_creacion datetime not null default getdate(),
  es_activo bit not null default 1
)
go

-- categorías de productos
create table categorias (
  id int identity(1,1) primary key,
  nombre varchar(50) not null unique,
  descripcion varchar(max)
)
go

-- proveedores de productos
create table proveedores (
  id int identity(1,1) primary key,
  nombre varchar(100) not null,
  telefono varchar(15),
  direccion varchar(200),
  correo varchar(100),
  ruc_nit varchar(20) not null unique
)
go

-- sucursales (ubicaciones físicas)
create table sucursales (
  id int identity(1,1) primary key,
  nombre varchar(100) not null,
  direccion varchar(200)
)
go

-- productos en inventario, con fecha de caducidad opcional
create table productos (
  id int identity(1,1) primary key,
  nombre varchar(100) not null,
  descripcion varchar(max),
  categoria_id int not null references categorias(id),
  precio_compra decimal(10,2),
  precio_venta decimal(10,2),
  stock_actual int not null default 0 check (stock_actual >= 0),
  stock_minimo int not null default 0 check (stock_minimo >= 0),
  fecha_caducidad date,
  codigo_de_barras varchar(50) not null unique,
  proveedor_id int not null references proveedores(id),
  sucursal_id int not null references sucursales(id)
)
go

-- movimientos de inventario: entradas, salidas, ajustes
create table movimientos (
  id int identity(1,1) primary key,
  tipo varchar(20) not null check (tipo in ('entrada','salida','ajuste')),
  cantidad int not null check (cantidad >= 0),
  fecha datetime not null default getdate(),
  usuario_id int not null references usuarios(id),
  producto_id int not null references productos(id),
  motivo varchar(max),
  sucursal_id int not null references sucursales(id)
)
go

-- alertas: stock bajo o caducidad
create table alertas (
  id int identity(1,1) primary key,
  producto_id int not null references productos(id),
  tipo varchar(20) not null check (tipo in ('stock_bajo','caducidad')),
  fecha_generada datetime not null default getdate(),
  leida bit not null default 0
)
go

-- auditoría de acciones críticas en el sistema
create table auditoria (
  id int identity(1,1) primary key,
  usuario_id int not null references usuarios(id),
  accion varchar(100) not null,
  fecha datetime not null default getdate(),
  tabla_afectada varchar(50) not null
)
go