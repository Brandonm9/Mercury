USE mercuryDB
GO

-- 1) Renombrar permisos existentes
UPDATE permisos
   SET nombre = 'productos.crear'
 WHERE nombre = 'crear_producto'
GO

UPDATE permisos
   SET nombre = 'productos.editar'
 WHERE nombre = 'editar_producto'
GO

UPDATE permisos
   SET nombre = 'productos.eliminar'
 WHERE nombre = 'eliminar_producto'
GO

-- 2) Crear el permiso de lista si no existe
IF NOT EXISTS (SELECT 1 FROM permisos WHERE nombre='productos.ver')
  INSERT INTO permisos (nombre, descripcion)
  VALUES ('productos.ver', 'Ver listado de productos')
GO

-- 3) Volver a asignar roles_permisos para que incluyan el permiso 'productos.ver'
-- 3a) Borra asignaciones antiguas para 'productos.ver' (por si acaso)
DELETE rp
  FROM roles_permisos rp
  JOIN permisos p ON rp.permiso_id = p.id
 WHERE p.nombre = 'productos.ver'
GO

-- 3b) Asigna 'productos.ver' a todos los roles que deban verlo
INSERT INTO roles_permisos (role_id, permiso_id)
SELECT r.id, p.id
  FROM roles r
  CROSS JOIN permisos p
 WHERE p.nombre = 'productos.ver'
   AND r.nombre IN ('administrador','gerente','empleado')
GO