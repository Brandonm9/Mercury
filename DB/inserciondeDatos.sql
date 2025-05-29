-------------------------------------------------------------------------------------------
--Llear las tablas
--Tablas de sucursales
INSERT INTO Sucursal (nombre, direccion)
VALUES ('Sucursal Central', 'Av. Libertad 123, Centro'),
    ('Sucursal Norte', 'Calle 5 #120, Zona Norte'),
    (
        'Sucursal Sur',
        'Blvd. del Sur 202, Zona Sur'
    ),
    (
        'Sucursal Este',
        'Carrera 11 #45, Barrio Este'
    ),
    (
        'Sucursal Oeste',
        'Avenida 7 #89, Barrio Oeste'
    );
--------------------------------------------------------
--tabla de usuarios
-- Empleados y gerentes para Sucursal Central (id=1)
INSERT INTO Usuario (nombre, correo, contrasena, rol, sucursal_id)
VALUES (
        'Juan P�rez',
        'juan.perez.central@correo.com',
        $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC23 ', ' Empleado ', 1),
(' Ana Torres ',   ' ana.torres.central @correo.com ',   ' $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC ', ' Empleado ', 1),
(' Carlos Ruiz ',  ' carlos.ruiz.central @correo.com ',  ' $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC ', ' Empleado ', 1),
(' Luisa G � mez ',  ' luisa.gomez.central @correo.com ', $2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC23',
        'Empleado',
        1
    ),
    (
        'Gloria Lara',
        'gloria.lara.central@correo.com',
        '$2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC',
        'Gerente',
        1
    );
-- Empleados y gerentes para Sucursal Norte (id=2)
INSERT INTO Usuario (nombre, correo, contrasena, rol, sucursal_id)
VALUES (
        'Mario L�pez',
        'mario.lopez.norte@correo.com',
        $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC23 ', ' Empleado ', 2),
(' Sara M � ndez ',   ' sara.mendez.norte @correo.com ',   $2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC23',
        'Empleado',
        2
    ),
    (
        'Pedro Salazar',
        'pedro.salazar.norte@correo.com',
        '$2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC',
        'Empleado',
        2
    ),
    (
        'Julia Castro',
        'julia.castro.norte@correo.com',
        '$2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC',
        'Empleado',
        2
    ),
    (
        'Esteban D�az',
        'esteban.diaz.norte@correo.com',
        $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC23 ', ' Gerente ',  2);

-- Empleados y gerentes para Sucursal Sur (id=3)
INSERT INTO Usuario (nombre, correo, contrasena, rol, sucursal_id) VALUES
(' Miguel Molina ',  ' miguel.molina.sur @correo.com ',    ' $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC ', ' Empleado ', 3),
(' Ver � nica Silva ', ' veronica.silva.sur @correo.com ',  $2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC23',
        'Empleado',
        3
    ),
    (
        'Ra�l Herrera',
        'raul.herrera.sur@correo.com',
        $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC23 ', ' Empleado ', 3),
(' Paula Cabrera ',  ' paula.cabrera.sur @correo.com ',    ' $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC ', ' Empleado ', 3),
(' Cristina Rivas ', ' cristina.rivas.sur @correo.com ',   ' $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC ', ' Gerente ',  3);

-- Empleados y gerentes para Sucursal Este (id=4)
INSERT INTO Usuario (nombre, correo, contrasena, rol, sucursal_id) VALUES
(' Fernando Ortiz ',   ' fernando.ortiz.este @correo.com ',   ' $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC ', ' Empleado ', 4),
(' Isabel Paredes ',   ' isabel.paredes.este @correo.com ',   ' $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC ', ' Empleado ', 4),
(' Emilio Guzm � n ',    ' emilio.guzman.este @correo.com ',   $2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC23',
        'Empleado',
        4
    ),
    (
        'Laura Villalta',
        'laura.villalta.este@correo.com',
        '$2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC',
        'Empleado',
        4
    ),
    (
        'H�ctor Romero',
        'hector.romero.este@correo.com',
        $2b$12$wr2SNRv6PY7KJ / NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC23 ', ' Gerente ',  4);

-- Empleados y gerentes para Sucursal Oeste (id=5)
INSERT INTO Usuario (nombre, correo, contrasena, rol, sucursal_id) VALUES
(' Patricia Rold � n ',  ' patricia.roldan.oeste @correo.com ',$2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC23',
        'Empleado',
        5
    ),
    (
        'Gabriel Funes',
        'gabriel.funes.oeste@correo.com',
        '$2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC',
        'Empleado',
        5
    ),
    (
        'Alicia Campos',
        'alicia.campos.oeste@correo.com',
        '$2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC',
        'Empleado',
        5
    ),
    (
        'David Castillo',
        'david.castillo.oeste@correo.com',
        '$2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC',
        'Empleado',
        5
    ),
    (
        'Rosa Moreno',
        'rosa.moreno.oeste@correo.com',
        '$2b$12$wr2SNRv6PY7KJ/NwnWW0F.mC89A8mtxalJr3OL1H6eK5zPCCvZmNC',
        'Gerente',
        5
    );
-- Administrador global (sucursal_id = NULL)
INSERT INTO Usuario (nombre, correo, contrasena, rol, sucursal_id)
VALUES (
        'Administrador General',
        'admin.general@correo.com',
        'admin123',
        'Administrador',
        NULL
    );
-------------------------------------------------------------------------------------------
--Catergoria
INSERT INTO Categoria (nombre, descripcion)
VALUES (
        'Bebidas',
        'Incluye refrescos, jugos, aguas y energizantes'
    ),
    (
        'Snacks',
        'Botanas, papas, chocolates y barras energ�ticas'
    ),
    ('L�cteos', 'Leche, yogurt, quesos y derivados'),
    (
        'Abarrotes',
        'Productos b�sicos de despensa: arroz, az�car, sal, pastas, etc.'
    ),
    (
        'Limpieza',
        'Detergentes, desinfectantes, jabones y productos de higiene'
    ),
    (
        'Panader�a',
        'Pan dulce, pan de caja, boller�a y productos horneados'
    );
-------------------------------------------------------------------------------------------
--Proveedores
INSERT INTO Proveedor (nombre, telefono, direccion, correo, RUC_NIT)
VALUES (
        'Distribuidora Bebidas S.A.',
        '2222-1111',
        'Av. Principal 101',
        'contacto@bebidas.com',
        'RUC10001'
    ),
    (
        'Snacks Express',
        '2333-2222',
        'Calle Botanas 22',
        'ventas@snacksexpress.com',
        'RUC10002'
    ),
    (
        'L�cteos Del Campo',
        '2444-3333',
        'Ruta Lechera 77',
        'info@lacteosdelcampo.com',
        'RUC10003'
    ),
    (
        'Abarrotes Global',
        '2555-4444',
        'Boulevard Central 50',
        'abasto@abarrotesglobal.com',
        'RUC10004'
    ),
    (
        'Distribuidora Limpia',
        '2666-5555',
        'Zona Higiene 18',
        'servicio@limpia.com',
        'RUC10005'
    );
-------------------------------------------------------------------------------------------
--productos
INSERT INTO Producto (nombre, categoria_id, proveedor_id)
VALUES -- Bebidas (1)
    ('Coca-Cola 500ml', 1, 1),
    ('Pepsi 500ml', 1, 1),
    ('Agua Pura 1L', 1, 1),
    ('Red Bull 250ml', 1, 1),
    ('Jugo de Naranja 500ml', 1, 1),
    -- Snacks (2)
    ('Papas Lays 30g', 2, 2),
    ('Chocolatina Jet', 2, 2),
    ('Barra Granola', 2, 2),
    ('Cheetos 35g', 2, 2),
    ('Galletas Oreo', 2, 2),
    -- L�cteos (3)
    ('Leche Entera 1L', 3, 3),
    ('Yogurt Natural 200ml', 3, 3),
    ('Queso Fresco 250g', 3, 3),
    ('Mantequilla 100g', 3, 3),
    ('Leche Descremada 1L', 3, 3),
    -- Abarrotes (4)
    ('Arroz 1kg', 4, 4),
    ('Az�car 1kg', 4, 4),
    ('Sal Refinada 500g', 4, 4),
    ('Espaguetis 400g', 4, 4),
    ('Frijoles Negros 500g', 4, 4),
    -- Limpieza (5)
    ('Detergente L�quido 1L', 5, 5),
    ('Jab�n en Barra', 5, 5),
    ('Cloro 1L', 5, 5),
    ('Toalla de Papel', 5, 5),
    ('Desinfectante 500ml', 5, 5),
    -- Panader�a (6)
    ('Pan de Caja Blanco', 6, 4),
    ('Pan Dulce', 6, 4),
    ('Croissant', 6, 4),
    ('Bollos Integrales', 6, 4),
    ('Pan Franc�s', 6, 4);
-------------------------------------------------------------------------------------------
--Productos por sucursal
-- Sucursal Central (id=1)
INSERT INTO ProductoSucursal (
        sucursal_id,
        producto_id,
        stock_actual,
        stock_minimo
    )
VALUES (1, 1, 50, 10),
    -- Coca-Cola 500ml
    (1, 2, 40, 10),
    -- Pepsi 500ml
    (1, 3, 70, 15),
    -- Agua Pura 1L
    (1, 4, 30, 8),
    -- Red Bull 250ml
    (1, 5, 25, 5),
    -- Jugo de Naranja
    (1, 6, 80, 20),
    -- Papas Lays
    (1, 7, 60, 10),
    -- Chocolatina Jet
    (1, 8, 45, 10),
    -- Barra Granola
    (1, 9, 55, 15),
    -- Cheetos
    (1, 10, 90, 25),
    -- Galletas Oreo
    (1, 11, 60, 15),
    -- Leche Entera
    (1, 16, 40, 10),
    -- Arroz 1kg
    (1, 21, 30, 8),
    -- Detergente L�quido
    (1, 26, 60, 15),
    -- Pan de Caja Blanco
    (1, 27, 45, 12);
-- Pan Dulce
-- Sucursal Norte (id=2)
INSERT INTO ProductoSucursal (
        sucursal_id,
        producto_id,
        stock_actual,
        stock_minimo
    )
VALUES (2, 1, 35, 10),
    (2, 2, 25, 8),
    (2, 3, 60, 15),
    (2, 6, 70, 20),
    (2, 8, 40, 10),
    (2, 10, 80, 25),
    (2, 11, 55, 15),
    (2, 12, 45, 10),
    (2, 13, 30, 8),
    (2, 16, 50, 12),
    (2, 18, 25, 8),
    (2, 21, 38, 9),
    (2, 22, 42, 8),
    (2, 26, 45, 12),
    (2, 28, 50, 14);
--Sucursal (id=3)
INSERT INTO ProductoSucursal (
        sucursal_id,
        producto_id,
        stock_actual,
        stock_minimo
    )
VALUES (3, 2, 40, 10),
    -- Pepsi 500ml
    (3, 3, 55, 12),
    -- Agua Pura 1L
    (3, 4, 28, 6),
    -- Red Bull 250ml
    (3, 5, 20, 4),
    -- Jugo de Naranja
    (3, 7, 65, 15),
    -- Chocolatina Jet
    (3, 8, 35, 8),
    -- Barra Granola
    (3, 9, 60, 15),
    -- Cheetos
    (3, 12, 50, 12),
    -- Yogurt Natural
    (3, 13, 32, 6),
    -- Queso Fresco
    (3, 14, 30, 8),
    -- Mantequilla
    (3, 17, 28, 8),
    -- Az�car 1kg
    (3, 19, 22, 5),
    -- Espaguetis
    (3, 22, 30, 8),
    -- Jab�n en Barra
    (3, 26, 50, 14),
    -- Pan de Caja Blanco
    (3, 29, 38, 9);
-- Bollos Integrales
--Sucursal (id=4)
INSERT INTO ProductoSucursal (
        sucursal_id,
        producto_id,
        stock_actual,
        stock_minimo
    )
VALUES (4, 1, 48, 10),
    -- Coca-Cola 500ml
    (4, 3, 65, 13),
    -- Agua Pura 1L
    (4, 5, 20, 5),
    -- Jugo de Naranja
    (4, 6, 62, 12),
    -- Papas Lays
    (4, 8, 30, 7),
    -- Barra Granola
    (4, 10, 85, 20),
    -- Galletas Oreo
    (4, 11, 70, 16),
    -- Leche Entera 1L
    (4, 13, 25, 6),
    -- Queso Fresco
    (4, 15, 40, 10),
    -- Leche Descremada
    (4, 17, 40, 10),
    -- Az�car 1kg
    (4, 18, 35, 8),
    -- Sal Refinada
    (4, 21, 25, 7),
    -- Detergente L�quido
    (4, 23, 33, 10),
    -- Cloro 1L
    (4, 27, 42, 12),
    -- Pan Dulce
    (4, 30, 36, 8);
-- Pan Franc�s
--sucursal (id=5)
INSERT INTO ProductoSucursal (
        sucursal_id,
        producto_id,
        stock_actual,
        stock_minimo
    )
VALUES (5, 1, 40, 10),
    -- Coca-Cola 500ml
    (5, 2, 38, 10),
    -- Pepsi 500ml
    (5, 4, 24, 5),
    -- Red Bull 250ml
    (5, 6, 70, 20),
    -- Papas Lays
    (5, 7, 50, 10),
    -- Chocolatina Jet
    (5, 9, 45, 10),
    -- Cheetos
    (5, 12, 43, 10),
    -- Yogurt Natural
    (5, 14, 32, 7),
    -- Mantequilla
    (5, 15, 28, 7),
    -- Leche Descremada
    (5, 17, 44, 10),
    -- Az�car 1kg
    (5, 19, 35, 8),
    -- Espaguetis
    (5, 22, 37, 10),
    -- Jab�n en Barra
    (5, 24, 41, 9),
    -- Toalla de Papel
    (5, 28, 39, 8),
    -- Croissant
    (5, 30, 35, 8);
-- Pan Franc�s
-------------------------------------------------------------------------------------------
--Ingresar datos de movimientos
--sucursal del central (id=1)
-- Lunes 2025-05-12
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        20,
        '2025-05-12 09:05',
        1,
        1,
        'Reposici�n de stock Coca-Cola'
    ),
    (
        'salida',
        10,
        '2025-05-12 11:12',
        2,
        6,
        'Venta de Papas Lays'
    ),
    (
        'salida',
        8,
        '2025-05-12 12:35',
        3,
        11,
        'Venta de Leche Entera'
    ),
    (
        'entrada',
        25,
        '2025-05-12 14:07',
        4,
        16,
        'Compra de Arroz 1kg'
    ),
    (
        'salida',
        15,
        '2025-05-12 15:21',
        1,
        10,
        'Venta de Galletas Oreo'
    );
-- Martes 2025-05-13
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        5,
        '2025-05-13 09:55',
        2,
        8,
        'Venta de Barra Granola'
    ),
    (
        'entrada',
        12,
        '2025-05-13 10:21',
        3,
        21,
        'Ingreso Detergente L�quido'
    ),
    (
        'salida',
        13,
        '2025-05-13 12:40',
        4,
        2,
        'Venta de Pepsi 500ml'
    ),
    (
        'entrada',
        18,
        '2025-05-13 13:32',
        5,
        3,
        'Ingreso Agua Pura 1L'
    ),
    (
        'salida',
        9,
        '2025-05-13 16:13',
        2,
        27,
        'Venta de Pan Dulce'
    );
-- Mi�rcoles 2025-05-14
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        15,
        '2025-05-14 08:54',
        1,
        7,
        'Ingreso Chocolatina Jet'
    ),
    (
        'salida',
        12,
        '2025-05-14 11:23',
        3,
        1,
        'Venta de Coca-Cola 500ml'
    ),
    (
        'entrada',
        20,
        '2025-05-14 12:30',
        5,
        11,
        'Ingreso Leche Entera 1L'
    ),
    (
        'salida',
        7,
        '2025-05-14 13:50',
        4,
        6,
        'Venta de Papas Lays'
    ),
    (
        'entrada',
        9,
        '2025-05-14 16:15',
        2,
        8,
        'Ingreso Barra Granola'
    );
-- Jueves 2025-05-15
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        10,
        '2025-05-15 09:45',
        3,
        16,
        'Venta de Arroz 1kg'
    ),
    (
        'salida',
        12,
        '2025-05-15 10:20',
        2,
        26,
        'Venta de Pan de Caja'
    ),
    (
        'entrada',
        17,
        '2025-05-15 11:15',
        5,
        27,
        'Ingreso Pan Dulce'
    ),
    (
        'salida',
        6,
        '2025-05-15 13:07',
        1,
        9,
        'Venta de Cheetos'
    ),
    (
        'entrada',
        8,
        '2025-05-15 14:50',
        4,
        10,
        'Ingreso Galletas Oreo'
    );
-- Viernes 2025-05-16
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        8,
        '2025-05-16 10:05',
        2,
        21,
        'Venta de Detergente'
    ),
    (
        'salida',
        9,
        '2025-05-16 10:40',
        3,
        7,
        'Venta de Chocolatina Jet'
    ),
    (
        'entrada',
        16,
        '2025-05-16 11:28',
        1,
        3,
        'Ingreso Agua Pura 1L'
    ),
    (
        'salida',
        5,
        '2025-05-16 12:55',
        5,
        11,
        'Venta de Leche Entera'
    ),
    (
        'entrada',
        14,
        '2025-05-16 13:33',
        4,
        26,
        'Ingreso Pan de Caja'
    );
-- S�bado 2025-05-17
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        20,
        '2025-05-17 09:25',
        1,
        6,
        'Ingreso Papas Lays'
    ),
    (
        'salida',
        6,
        '2025-05-17 11:49',
        2,
        9,
        'Venta de Cheetos'
    ),
    (
        'entrada',
        12,
        '2025-05-17 13:15',
        3,
        16,
        'Ingreso Arroz 1kg'
    ),
    (
        'salida',
        8,
        '2025-05-17 15:17',
        4,
        8,
        'Venta de Barra Granola'
    ),
    (
        'entrada',
        13,
        '2025-05-17 16:10',
        5,
        10,
        'Ingreso Galletas Oreo'
    );
-- Domingo 2025-05-18
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        10,
        '2025-05-18 09:40',
        1,
        26,
        'Venta Pan de Caja'
    ),
    (
        'entrada',
        8,
        '2025-05-18 10:28',
        2,
        27,
        'Ingreso Pan Dulce'
    ),
    (
        'salida',
        7,
        '2025-05-18 11:39',
        3,
        21,
        'Venta Detergente'
    ),
    (
        'entrada',
        15,
        '2025-05-18 12:55',
        4,
        1,
        'Ingreso Coca-Cola 500ml'
    ),
    (
        'salida',
        8,
        '2025-05-18 14:22',
        5,
        16,
        'Venta Arroz 1kg'
    );
-------------------------------------------------------------------------------------------
-- Sucursal Norte (id=2)
-- Lunes 2025-05-12
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        18,
        '2025-05-12 09:10',
        6,
        16,
        'Reposici�n de stock Arroz 1kg'
    ),
    (
        'salida',
        12,
        '2025-05-12 10:25',
        7,
        3,
        'Venta de Agua Pura 1L'
    ),
    (
        'salida',
        7,
        '2025-05-12 11:40',
        8,
        10,
        'Venta de Galletas Oreo'
    ),
    (
        'entrada',
        14,
        '2025-05-12 13:00',
        9,
        18,
        'Ingreso Sal Refinada'
    ),
    (
        'salida',
        10,
        '2025-05-12 15:30',
        10,
        6,
        'Venta de Papas Lays'
    );
-- Martes 2025-05-13
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        15,
        '2025-05-13 09:35',
        7,
        21,
        'Ingreso Detergente L�quido'
    ),
    (
        'salida',
        11,
        '2025-05-13 10:42',
        8,
        2,
        'Venta de Pepsi 500ml'
    ),
    (
        'salida',
        9,
        '2025-05-13 12:18',
        9,
        26,
        'Venta de Pan de Caja'
    ),
    (
        'entrada',
        20,
        '2025-05-13 13:21',
        10,
        17,
        'Ingreso Az�car 1kg'
    ),
    (
        'salida',
        6,
        '2025-05-13 16:09',
        6,
        1,
        'Venta de Coca-Cola 500ml'
    );
-- Mi�rcoles 2025-05-14
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        11,
        '2025-05-14 09:20',
        7,
        8,
        'Ingreso Barra Granola'
    ),
    (
        'salida',
        8,
        '2025-05-14 10:58',
        8,
        10,
        'Venta de Galletas Oreo'
    ),
    (
        'entrada',
        17,
        '2025-05-14 12:41',
        9,
        12,
        'Ingreso Yogurt Natural'
    ),
    (
        'salida',
        10,
        '2025-05-14 13:55',
        10,
        11,
        'Venta de Leche Entera'
    ),
    (
        'entrada',
        16,
        '2025-05-14 16:30',
        6,
        27,
        'Ingreso Pan Dulce'
    );
-- Jueves 2025-05-15
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        9,
        '2025-05-15 09:05',
        7,
        17,
        'Venta de Az�car 1kg'
    ),
    (
        'entrada',
        13,
        '2025-05-15 10:18',
        8,
        2,
        'Ingreso Pepsi 500ml'
    ),
    (
        'salida',
        7,
        '2025-05-15 11:22',
        9,
        8,
        'Venta Barra Granola'
    ),
    (
        'entrada',
        18,
        '2025-05-15 14:00',
        10,
        21,
        'Ingreso Detergente L�quido'
    ),
    (
        'salida',
        12,
        '2025-05-15 15:45',
        6,
        26,
        'Venta Pan de Caja'
    );
-- Viernes 2025-05-16
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        14,
        '2025-05-16 09:37',
        7,
        3,
        'Ingreso Agua Pura 1L'
    ),
    (
        'salida',
        5,
        '2025-05-16 10:55',
        8,
        6,
        'Venta Papas Lays'
    ),
    (
        'entrada',
        12,
        '2025-05-16 13:19',
        9,
        11,
        'Ingreso Leche Entera'
    ),
    (
        'salida',
        9,
        '2025-05-16 14:25',
        10,
        9,
        'Venta Cheetos'
    ),
    (
        'entrada',
        10,
        '2025-05-16 15:10',
        6,
        12,
        'Ingreso Yogurt Natural'
    );
-- S�bado 2025-05-17
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        8,
        '2025-05-17 09:22',
        7,
        1,
        'Venta Coca-Cola 500ml'
    ),
    (
        'entrada',
        16,
        '2025-05-17 10:39',
        8,
        16,
        'Ingreso Arroz 1kg'
    ),
    (
        'salida',
        10,
        '2025-05-17 12:06',
        9,
        18,
        'Venta Sal Refinada'
    ),
    (
        'entrada',
        19,
        '2025-05-17 13:30',
        10,
        27,
        'Ingreso Pan Dulce'
    ),
    (
        'salida',
        7,
        '2025-05-17 15:03',
        6,
        8,
        'Venta Barra Granola'
    );
-- Domingo 2025-05-18
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        12,
        '2025-05-18 08:50',
        7,
        21,
        'Ingreso Detergente L�quido'
    ),
    (
        'salida',
        11,
        '2025-05-18 10:23',
        8,
        3,
        'Venta Agua Pura 1L'
    ),
    (
        'entrada',
        13,
        '2025-05-18 11:48',
        9,
        26,
        'Ingreso Pan de Caja'
    ),
    (
        'salida',
        6,
        '2025-05-18 13:20',
        10,
        17,
        'Venta Az�car 1kg'
    ),
    (
        'entrada',
        14,
        '2025-05-18 14:12',
        6,
        11,
        'Ingreso Leche Entera'
    );
-------------------------------------------------------------------------------------------
-- Sucursal Sur (id=3)
-- Lunes 2025-05-12
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        16,
        '2025-05-12 09:18',
        11,
        2,
        'Reposici�n Pepsi 500ml'
    ),
    (
        'salida',
        9,
        '2025-05-12 10:33',
        12,
        8,
        'Venta Barra Granola'
    ),
    (
        'entrada',
        14,
        '2025-05-12 11:47',
        13,
        13,
        'Ingreso Queso Fresco'
    ),
    (
        'salida',
        11,
        '2025-05-12 13:15',
        14,
        19,
        'Venta Espaguetis'
    ),
    (
        'salida',
        8,
        '2025-05-12 15:10',
        15,
        7,
        'Venta Chocolatina Jet'
    );
-- Martes 2025-05-13
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        18,
        '2025-05-13 09:20',
        12,
        12,
        'Ingreso Yogurt Natural'
    ),
    (
        'salida',
        7,
        '2025-05-13 10:57',
        13,
        28,
        'Venta Croissant'
    ),
    (
        'entrada',
        15,
        '2025-05-13 12:38',
        14,
        9,
        'Ingreso Cheetos'
    ),
    (
        'salida',
        9,
        '2025-05-13 13:55',
        15,
        29,
        'Venta Bollos Integrales'
    ),
    (
        'entrada',
        13,
        '2025-05-13 15:40',
        11,
        14,
        'Ingreso Mantequilla'
    );
-- Mi�rcoles 2025-05-14
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        10,
        '2025-05-14 09:45',
        12,
        2,
        'Venta Pepsi 500ml'
    ),
    (
        'entrada',
        19,
        '2025-05-14 10:50',
        13,
        8,
        'Ingreso Barra Granola'
    ),
    (
        'salida',
        11,
        '2025-05-14 12:16',
        14,
        12,
        'Venta Yogurt Natural'
    ),
    (
        'entrada',
        14,
        '2025-05-14 13:22',
        15,
        17,
        'Ingreso Az�car 1kg'
    ),
    (
        'salida',
        8,
        '2025-05-14 14:41',
        11,
        13,
        'Venta Queso Fresco'
    );
-- Jueves 2025-05-15
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        12,
        '2025-05-15 09:28',
        12,
        19,
        'Ingreso Espaguetis'
    ),
    (
        'salida',
        9,
        '2025-05-15 10:55',
        13,
        9,
        'Venta Cheetos'
    ),
    (
        'entrada',
        15,
        '2025-05-15 12:19',
        14,
        14,
        'Ingreso Mantequilla'
    ),
    (
        'salida',
        6,
        '2025-05-15 13:44',
        15,
        7,
        'Venta Chocolatina Jet'
    ),
    (
        'entrada',
        10,
        '2025-05-15 15:01',
        11,
        29,
        'Ingreso Bollos Integrales'
    );
-- Viernes 2025-05-16
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        12,
        '2025-05-16 09:55',
        12,
        28,
        'Venta Croissant'
    ),
    (
        'entrada',
        13,
        '2025-05-16 11:14',
        13,
        17,
        'Ingreso Az�car 1kg'
    ),
    (
        'salida',
        7,
        '2025-05-16 12:38',
        14,
        2,
        'Venta Pepsi 500ml'
    ),
    (
        'entrada',
        17,
        '2025-05-16 13:26',
        15,
        8,
        'Ingreso Barra Granola'
    ),
    (
        'salida',
        10,
        '2025-05-16 15:47',
        11,
        13,
        'Venta Queso Fresco'
    );
-- S�bado 2025-05-17
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        18,
        '2025-05-17 09:39',
        12,
        12,
        'Ingreso Yogurt Natural'
    ),
    (
        'salida',
        11,
        '2025-05-17 10:56',
        13,
        29,
        'Venta Bollos Integrales'
    ),
    (
        'entrada',
        12,
        '2025-05-17 12:05',
        14,
        19,
        'Ingreso Espaguetis'
    ),
    (
        'salida',
        8,
        '2025-05-17 13:18',
        15,
        7,
        'Venta Chocolatina Jet'
    ),
    (
        'entrada',
        13,
        '2025-05-17 14:44',
        11,
        28,
        'Ingreso Croissant'
    );
-- Domingo 2025-05-18
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        10,
        '2025-05-18 09:12',
        12,
        9,
        'Venta Cheetos'
    ),
    (
        'entrada',
        17,
        '2025-05-18 10:35',
        13,
        14,
        'Ingreso Mantequilla'
    ),
    (
        'salida',
        6,
        '2025-05-18 12:20',
        14,
        12,
        'Venta Yogurt Natural'
    ),
    (
        'entrada',
        15,
        '2025-05-18 13:59',
        15,
        13,
        'Ingreso Queso Fresco'
    ),
    (
        'salida',
        8,
        '2025-05-18 15:30',
        11,
        28,
        'Venta Croissant'
    );
-------------------------------------------------------------------------------------------
-- Sucursal Este (id=4)
-- Lunes 2025-05-12
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        14,
        '2025-05-12 08:57',
        16,
        1,
        'Ingreso Coca-Cola 500ml'
    ),
    (
        'salida',
        9,
        '2025-05-12 10:22',
        17,
        6,
        'Venta Papas Lays'
    ),
    (
        'entrada',
        15,
        '2025-05-12 11:34',
        18,
        13,
        'Ingreso Queso Fresco'
    ),
    (
        'salida',
        12,
        '2025-05-12 13:09',
        19,
        21,
        'Venta Detergente L�quido'
    ),
    (
        'salida',
        8,
        '2025-05-12 14:50',
        20,
        18,
        'Venta Sal Refinada'
    );
-- Martes 2025-05-13
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        13,
        '2025-05-13 09:28',
        17,
        10,
        'Ingreso Galletas Oreo'
    ),
    (
        'salida',
        10,
        '2025-05-13 10:46',
        18,
        23,
        'Venta Cloro 1L'
    ),
    (
        'entrada',
        12,
        '2025-05-13 12:31',
        19,
        11,
        'Ingreso Leche Entera 1L'
    ),
    (
        'salida',
        7,
        '2025-05-13 13:59',
        20,
        26,
        'Venta Pan de Caja'
    ),
    (
        'entrada',
        16,
        '2025-05-13 15:13',
        16,
        27,
        'Ingreso Pan Dulce'
    );
-- Mi�rcoles 2025-05-14
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        11,
        '2025-05-14 09:20',
        17,
        1,
        'Venta Coca-Cola 500ml'
    ),
    (
        'entrada',
        14,
        '2025-05-14 10:53',
        18,
        6,
        'Ingreso Papas Lays'
    ),
    (
        'salida',
        8,
        '2025-05-14 12:05',
        19,
        11,
        'Venta Leche Entera 1L'
    ),
    (
        'entrada',
        15,
        '2025-05-14 13:48',
        20,
        13,
        'Ingreso Queso Fresco'
    ),
    (
        'salida',
        10,
        '2025-05-14 15:14',
        16,
        10,
        'Venta Galletas Oreo'
    );
-- Jueves 2025-05-15
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        12,
        '2025-05-15 09:40',
        17,
        21,
        'Ingreso Detergente L�quido'
    ),
    (
        'salida',
        9,
        '2025-05-15 11:12',
        18,
        23,
        'Venta Cloro 1L'
    ),
    (
        'entrada',
        11,
        '2025-05-15 12:22',
        19,
        18,
        'Ingreso Sal Refinada'
    ),
    (
        'salida',
        8,
        '2025-05-15 13:55',
        20,
        6,
        'Venta Papas Lays'
    ),
    (
        'entrada',
        13,
        '2025-05-15 15:33',
        16,
        10,
        'Ingreso Galletas Oreo'
    );
-- Viernes 2025-05-16
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        12,
        '2025-05-16 09:58',
        17,
        26,
        'Venta Pan de Caja'
    ),
    (
        'entrada',
        14,
        '2025-05-16 11:41',
        18,
        27,
        'Ingreso Pan Dulce'
    ),
    (
        'salida',
        7,
        '2025-05-16 12:57',
        19,
        1,
        'Venta Coca-Cola 500ml'
    ),
    (
        'entrada',
        15,
        '2025-05-16 13:39',
        20,
        13,
        'Ingreso Queso Fresco'
    ),
    (
        'salida',
        8,
        '2025-05-16 15:20',
        16,
        18,
        'Venta Sal Refinada'
    );
-- S�bado 2025-05-17
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        17,
        '2025-05-17 09:12',
        17,
        11,
        'Ingreso Leche Entera 1L'
    ),
    (
        'salida',
        11,
        '2025-05-17 10:28',
        18,
        21,
        'Venta Detergente L�quido'
    ),
    (
        'entrada',
        10,
        '2025-05-17 12:14',
        19,
        23,
        'Ingreso Cloro 1L'
    ),
    (
        'salida',
        7,
        '2025-05-17 13:36',
        20,
        26,
        'Venta Pan de Caja'
    ),
    (
        'entrada',
        12,
        '2025-05-17 15:11',
        16,
        6,
        'Ingreso Papas Lays'
    );
-- Domingo 2025-05-18
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        13,
        '2025-05-18 09:29',
        17,
        10,
        'Venta Galletas Oreo'
    ),
    (
        'entrada',
        14,
        '2025-05-18 10:55',
        18,
        27,
        'Ingreso Pan Dulce'
    ),
    (
        'salida',
        8,
        '2025-05-18 12:22',
        19,
        1,
        'Venta Coca-Cola 500ml'
    ),
    (
        'entrada',
        11,
        '2025-05-18 13:40',
        20,
        21,
        'Ingreso Detergente L�quido'
    ),
    (
        'salida',
        9,
        '2025-05-18 15:17',
        16,
        18,
        'Venta Sal Refinada'
    );
-------------------------------------------------------------------------------------------
-- Sucursal Oeste (id=5)
-- Lunes 2025-05-12
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        18,
        '2025-05-12 09:10',
        21,
        6,
        'Ingreso Papas Lays'
    ),
    (
        'salida',
        10,
        '2025-05-12 10:23',
        22,
        7,
        'Venta Chocolatina Jet'
    ),
    (
        'entrada',
        14,
        '2025-05-12 11:45',
        23,
        14,
        'Ingreso Mantequilla'
    ),
    (
        'salida',
        12,
        '2025-05-12 13:00',
        24,
        19,
        'Venta Espaguetis'
    ),
    (
        'salida',
        8,
        '2025-05-12 14:25',
        25,
        9,
        'Venta Cheetos'
    );
-- Martes 2025-05-13
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        13,
        '2025-05-13 09:39',
        22,
        12,
        'Ingreso Yogurt Natural'
    ),
    (
        'salida',
        9,
        '2025-05-13 10:54',
        23,
        29,
        'Venta Bollos Integrales'
    ),
    (
        'entrada',
        15,
        '2025-05-13 12:33',
        24,
        8,
        'Ingreso Barra Granola'
    ),
    (
        'salida',
        7,
        '2025-05-13 13:42',
        25,
        28,
        'Venta Croissant'
    ),
    (
        'entrada',
        10,
        '2025-05-13 15:09',
        21,
        24,
        'Ingreso Toalla de Papel'
    );
-- Mi�rcoles 2025-05-14
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        12,
        '2025-05-14 09:22',
        22,
        14,
        'Venta Mantequilla'
    ),
    (
        'entrada',
        18,
        '2025-05-14 10:35',
        23,
        15,
        'Ingreso Leche Descremada'
    ),
    (
        'salida',
        11,
        '2025-05-14 12:19',
        24,
        7,
        'Venta Chocolatina Jet'
    ),
    (
        'entrada',
        13,
        '2025-05-14 13:54',
        25,
        12,
        'Ingreso Yogurt Natural'
    ),
    (
        'salida',
        10,
        '2025-05-14 15:10',
        21,
        8,
        'Venta Barra Granola'
    );
-- Jueves 2025-05-15
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        16,
        '2025-05-15 09:44',
        22,
        6,
        'Ingreso Papas Lays'
    ),
    (
        'salida',
        8,
        '2025-05-15 11:07',
        23,
        9,
        'Venta Cheetos'
    ),
    (
        'entrada',
        12,
        '2025-05-15 12:23',
        24,
        29,
        'Ingreso Bollos Integrales'
    ),
    (
        'salida',
        7,
        '2025-05-15 13:50',
        25,
        24,
        'Venta Toalla de Papel'
    ),
    (
        'entrada',
        15,
        '2025-05-15 15:20',
        21,
        28,
        'Ingreso Croissant'
    );
-- Viernes 2025-05-16
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        10,
        '2025-05-16 09:55',
        22,
        19,
        'Venta Espaguetis'
    ),
    (
        'entrada',
        13,
        '2025-05-16 11:17',
        23,
        7,
        'Ingreso Chocolatina Jet'
    ),
    (
        'salida',
        6,
        '2025-05-16 12:45',
        24,
        14,
        'Venta Mantequilla'
    ),
    (
        'entrada',
        17,
        '2025-05-16 13:38',
        25,
        15,
        'Ingreso Leche Descremada'
    ),
    (
        'salida',
        8,
        '2025-05-16 15:11',
        21,
        12,
        'Venta Yogurt Natural'
    );
-- S�bado 2025-05-17
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'entrada',
        14,
        '2025-05-17 09:19',
        22,
        29,
        'Ingreso Bollos Integrales'
    ),
    (
        'salida',
        11,
        '2025-05-17 10:40',
        23,
        28,
        'Venta Croissant'
    ),
    (
        'entrada',
        10,
        '2025-05-17 12:07',
        24,
        24,
        'Ingreso Toalla de Papel'
    ),
    (
        'salida',
        7,
        '2025-05-17 13:33',
        25,
        9,
        'Venta Cheetos'
    ),
    (
        'entrada',
        12,
        '2025-05-17 15:12',
        21,
        14,
        'Ingreso Mantequilla'
    );
-- Domingo 2025-05-18
INSERT INTO Movimiento (
        tipo,
        cantidad,
        fecha,
        usuario_id,
        producto_sucursal_id,
        motivo
    )
VALUES (
        'salida',
        13,
        '2025-05-18 09:41',
        22,
        12,
        'Venta Yogurt Natural'
    ),
    (
        'entrada',
        15,
        '2025-05-18 10:53',
        23,
        15,
        'Ingreso Leche Descremada'
    ),
    (
        'salida',
        9,
        '2025-05-18 12:11',
        24,
        24,
        'Venta Toalla de Papel'
    ),
    (
        'entrada',
        10,
        '2025-05-18 13:27',
        25,
        6,
        'Ingreso Papas Lays'
    ),
    (
        'salida',
        8,
        '2025-05-18 15:08',
        21,
        7,
        'Venta Chocolatina Jet'
    );
GO