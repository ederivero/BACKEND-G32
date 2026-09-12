CREATE TABLE IF NOT EXISTS clientes (
	id SERIAL PRIMARY KEY,
	nombre TEXT NOT NULL,
	ciudad TEXT
);

CREATE TABLE IF NOT EXISTS pedidos (
	id SERIAL PRIMARY KEY,
	total NUMERIC(2),
	fecha DATE DEFAULT CURRENT_DATE,
	cliente_id INT REFERENCES clientes(id) -- Asi se crea la relacion en la misma definicion de columna
	-- Si queremos crear la CONSTRAINT AL FINAL
    -- CONSTRAINT fk_cliente FOREIGN KEY client_id REFERENCES clientes(id)
);

-- Ctrl + Enter > Ejecuta la sentencia seleccionada o la sentencia donde se ubica el cursor
-- Ctrl + Shift + O > Muestra/Oculta la salida del servidor


INSERT INTO clientes (nombre, ciudad) VALUES
('Eduardo de Rivero', 'Arequipa'),
('Judith Tito', 'Lima'),
('Freddy Orihuela', 'Cusco'),
('Luis Villavicencio', 'Trujillo'),
('Manuel Rabanal', 'Apurimac'),
('Vanessa Gonzales', 'Cajamarca');


-- NUMERIC > puede recibir 2 parametros, en el cual si solo se le pasa 1 sera la cantidad de enteros
-- Y si se le pasa dos el primer parametro sera la cantidad de enteros y el segundo la cantidad de decimales
ALTER TABLE pedidos ALTER COLUMN total TYPE NUMERIC(10,2);



INSERT INTO pedidos (total, fecha, cliente_id) VALUES
(15345.56, DEFAULT, 1),
(456.45, '2026-08-10', 1),
(2948.00, '2026-09-01', 2),
(3345.23, '2026-04-02', 3),
(2222.12, '2026-05-05', 3),
(96576.90, '2026-07-27', 4),
(5680.25, '2026-08-14', 5),
(12376.29, '2026-08-31', 5);


INSERT INTO pedidos (total, fecha, cliente_id) VALUES
(999.99, DEFAULT, NULL);

-- Visualizar la data de dos o mas tablas
-- INNER JOIN (interseccion)
SELECT * FROM clientes INNER JOIN pedidos ON clientes.id = pedidos.cliente_id;


-- LEFT JOIN
SELECT * FROM clientes LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id ;


-- RIGHT JOIN
SELECT * FROM clientes RIGHT JOIN pedidos ON clientes.id = pedidos.cliente_id ;


-- FULL OUTER JOIN
SELECT * FROM clientes FULL OUTER JOIN pedidos ON clientes.id = pedidos.cliente_id ;


CREATE TABLE productos(
	id SERIAL PRIMARY KEY,
	nombre TEXT NOT NULL,
	precio_unitario NUMERIC(9,2),
	disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE detalle_pedidos(
	id SERIAL PRIMARY KEY,
	producto_id INT REFERENCES productos(id),
	cantidad INT,
	precio NUMERIC(9,2),
	pedido_id INT REFERENCES pedidos(id)
);



DELETE FROM pedidos;

INSERT INTO productos (nombre, precio_unitario, disponible) VALUES
('Laptop', 3500.00, TRUE),
('Mouse', 45.00, TRUE),
('Teclado', 120.00, TRUE),
('Monitor', 800.00, TRUE),
('Escritorio', 450.00, TRUE),
('Silla Gamer', 600.00, FALSE); 


INSERT INTO pedidos (total, fecha, cliente_id) VALUES
(3590.00, '2026-01-05', 1),  -- pedido 1: Laptop + Mouse
(120.00,  '2026-02-10', 2),  -- pedido 2: Teclado
(800.00,  '2026-02-15', 3),  -- pedido 3: Monitor
(800.00,  '2026-03-01', 4),  -- pedido 4: Monitor
(450.00,  '2026-03-03', NULL); -- pedido 5: sin cliente asignado

SELECT * FROM pedidos;

INSERT INTO detalle_pedidos (producto_id, cantidad, precio, pedido_id) VALUES
							(1, 				1, 	3500.00, 11),  -- Laptop en pedido 1 
							(2, 				2,  45.00,   11),  -- Mouse en pedido 1 (mismo pedido, 2 productos)
							(3, 				1,  120.00,  12),  -- Teclado en pedido 2
							(4, 				1,  800.00,  13),  -- Monitor en pedido 3
							(4, 				1,  800.00,  14),  -- Monitor en pedido 4
							(5, 				1,  450.00,  15);  -- Escritorio en pedido 5 (pedido sin cliente)


-- Ejercicios
-- 1. Listar el nombre del cliente y el total de cada de uno de sus pedidos
SELECT c.nombre, p.total 
FROM clientes c INNER JOIN pedidos p ON c.id = p.cliente_id;
					
-- 2. Listar todos los clientes con sus pedidos, aun asi no tengan ningun pedido
SELECT c.nombre, p.id 
FROM clientes AS c LEFT JOIN pedidos p ON p.cliente_id = c.id;

-- 3. Mostrar los clientes que nunca han pedido nada
SELECT c.nombre
FROM clientes c LEFT JOIN pedidos p ON p.cliente_id = c.id
WHERE p.id IS NULL;

-- 4. Encuentra los productos que nunca se han vendido (no estan presentes en detalle_pedidos)
SELECT p.nombre 
FROM productos p LEFT JOIN detalle_pedidos dp ON p.id = dp.producto_id 
WHERE dp.id IS NULL;

-- 5. Listar los productos marcados como no disponible
SELECT * FROM productos p WHERE p.disponible = FALSE;

