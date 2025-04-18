CREATE DATABASE mercuryDB
GO
USE mercuryDB
GO

-- Roles
CREATE ROLE Empleado;
CREATE ROLE Gerente;
CREATE ROLE Administrador;

-- Sucursales
CREATE TABLE Sucursal (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200) NOT NULL
);

-- Categorías
CREATE TABLE Categoria (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);

-- Proveedores
CREATE TABLE Proveedor (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(15),
    direccion VARCHAR(200),
    correo VARCHAR(100),
    RUC_NIT VARCHAR(20) UNIQUE
);

-- Productos
CREATE TABLE Producto (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria_id INT NOT NULL,
    proveedor_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES Categoria(id),
    FOREIGN KEY (proveedor_id) REFERENCES Proveedor(id)
);

-- Productos por Sucursal 
CREATE TABLE ProductoSucursal (
    id INT IDENTITY(1,1) PRIMARY KEY,
    sucursal_id INT NOT NULL,
    producto_id INT NOT NULL,
    stock_actual INT NOT NULL,
    stock_minimo INT NOT NULL,
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal(id),
    FOREIGN KEY (producto_id) REFERENCES Producto(id),
    CONSTRAINT UC_SucursalProducto UNIQUE (sucursal_id, producto_id)
);

-- Usuarios 
CREATE TABLE Usuario (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL CHECK (rol IN ('Empleado','Gerente','Administrador')),
    sucursal_id INT NULL, -- NULL si es admin que trabaja en todas
    fecha_creacion DATETIME NOT NULL DEFAULT GETDATE(),
    estado BIT NOT NULL DEFAULT 1,
    FOREIGN KEY (sucursal_id) REFERENCES Sucursal(id)
);

-- Movimientos de inventario por sucursal
CREATE TABLE Movimiento (
    id INT IDENTITY(1,1) PRIMARY KEY,
    tipo VARCHAR(20) NOT NULL CHECK (tipo IN ('entrada','salida')),
    cantidad INT NOT NULL,
    fecha DATETIME NOT NULL DEFAULT GETDATE(),
    usuario_id INT NOT NULL,
    producto_sucursal_id INT NOT NULL,
    motivo VARCHAR(255) NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
    FOREIGN KEY (producto_sucursal_id) REFERENCES ProductoSucursal(id)
);

-- Auditoría
CREATE TABLE Auditoria (
    id INT IDENTITY(1,1) PRIMARY KEY,
    usuario_id INT NOT NULL,
    accion VARCHAR(100) NOT NULL,
    fecha DATETIME NOT NULL DEFAULT GETDATE(),
    tabla_afectada VARCHAR(50) NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
);

-------------------------------------------------------------------------------------------
--Creacion de trigger
--Trigger actualizar stock en sucursales
GO
CREATE TRIGGER tr_ActualizarStockSucursal
ON Movimiento
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE ps
    SET stock_actual = 
        CASE 
            WHEN m.tipo = 'entrada' THEN ps.stock_actual + m.cantidad
            WHEN m.tipo = 'salida' THEN ps.stock_actual - m.cantidad
            ELSE ps.stock_actual
        END
    FROM ProductoSucursal ps
    JOIN inserted m ON ps.id = m.producto_sucursal_id;
END

--Trigger para autoria
GO
CREATE TRIGGER tr_AuditarMovimientos
ON Movimiento
AFTER INSERT
AS
BEGIN
  SET NOCOUNT ON;
  INSERT INTO Auditoria(usuario_id, accion, tabla_afectada)
  SELECT 
    usuario_id,
    CONCAT('Movimiento ID=', id, ' registrado'),
    'Movimiento'
  FROM inserted;
END
GO