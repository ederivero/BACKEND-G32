-- Continuando con el DML
-- UPDATE > actualizar los registros de las tablas
-- Si en el update no se pone condicionales se modificaran 
-- todos los registros
-- UPDATE nombre_tabla SET nombre = 'Ayudin' WHERE id = 1
UPDATE productos SET nombre = 'Arroz Faraon 5kg' WHERE id = 1;

-- Cada vez que se actualiza un registro , este NO VARIA su ubicacion de memoria pero psql
-- modifica el indice del registro que hace que se muestre al final

-- Actualizar el nombre de 'Cerveza Cusque¤a 620ml' a 'Cerveza Cusqueña 620ml'
UPDATE productos SET nombre ='Cerveza Cusqueña 620ml' 
WHERE nombre = 'Cerveza Cusque¤a 620ml';


-- DELETE
-- DELETE FROM nombre_tabla WHERE condicionales;
DELETE FROM productos WHERE id = 9;
SELECT * FROM productos;

-- La unica forma de revertir los cambios (UPDATE o DELETE) es si la query esta en una transaccion




