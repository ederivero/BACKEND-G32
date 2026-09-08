\c pruebas

-- DML : Data Manipulation Language (Lenguaje de Manipulacion de datos)
-- INSERT : Ingresar nuevos registros a una tabla 
-- SELECT : Obtener la informacion de determinados registros de una o varias tablas
-- UPDATE : Actualizar la informacion registrada
-- DELETE : Elimina de manera permanente los registros en base a condiciones

-- INSERT INTO nombre_tabla (nomb_col_1, nomb_col_2,...) VALUES (val_1, val_2, ...);
INSERT INTO personas (id, nombre, apellido, correo, fecha_nacimiento) VALUES
-- DEFAULT > Indicamos el valor por defecto definido en la columna
-- En las columnas SERIAL agarra el valor que le toca
-- En SQL comillas simples para informacion de texto, 
-- Comillas dobles para nombres de tablas, columnas, etc
-- En SQL Se usa el ISO 8601 para las fechas en el cual el formato es YYYY-MM-DD HH:MM:SS:mmmm
                     (DEFAULT, 'Eduardo', 'de Rivero', 'ederiveroman@gmail.com', '1999-12-31');

-- Si voy a insertar usando el orden de las columnas con el que la cree puedo precindir del nombre de las columnas PERO si o si tengo que declarar todas las columnas
INSERT INTO personas VALUES (DEFAULT, 'Martha', 'Escobedo', 'mescobedo@gmail.com', '2005-02-14'),
                            (DEFAULT, 'Rodrigo','Jimenez', 'rjimenez@gmail.com', '1989-06-15'),
                            (DEFAULT, 'Marge', 'Marquez', 'mmarquez@gmail.com', '2006-09-07');


-- Volviendo al DDL ALTER (Modificar la tabla)
-- Agregar columnas
-- Siempre ira al final, no se puede modificar el orden, si se puede hacer en MySQL - MariaDB 
-- ALTER TABLE personas ADD COLUMN sexo TEXT BEFORE | AFTER id;
ALTER TABLE personas ADD COLUMN sexo TEXT;

-- Eliminar columnas
-- NO EJECUTAR EL SIGUIENTE CODIGO:
ALTER TABLE personas DROP COLUMN fecha_nacimiento;

-- Cambiar el tipo de dato
-- Si vamos a cambiar de TEXT a INT entonces debemos de corroborar el cambio
ALTER TABLE personas ALTER COLUMN sexo TYPE INT USING sexo::INT;

-- Renombrar la columna
ALTER TABLE personas RENAME COLUMN sexo TO peso;




-- ==============================================================

-- SELECT (Visualizar los datos)
-- SELECT nomb_col1, nomb_col2, ... FROM tabla;
-- Ahora si queremos visualizar TODOS las columnas de la consulta
-- SELECT * FROM tabla;

SELECT nombre FROM personas;

SELECT * FROM personas;

-- Se le puede agregar condicionales para que los registros que cumplan esa condicion sean mostrados
SELECT * FROM personas WHERE id > 2;

SELECT * FROM personas WHERE id > 2 AND nombre = 'Rodrigo' OR nombre = 'Marge';


SELECT * FROM personas WHERE id > 2 AND nombre = 'rodrigo' OR nombre = 'Marge';
