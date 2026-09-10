-- En bd relaciones existen 3 tipos de relaciones entre tablas
-- 1 - 1
-- Es una relacion en la cual dos tablas tendran un registro que represente a la otran en un solo registro
-- Usuario tiene una perona
-- La clave foranea > Es la representacion del registro (pk) de la tabla A hacia la tabla B

-- La clave foranea (FK) no importa en cual de las dos tabla vaya 

-- 1 - n
-- Una persona tiene varias direcciones
-- La FK van en la tabla "varias", en este escenario la FK iria en la tabla de direcciones. Porque asi se
-- representa que ese registro le pertenece a una persona determinada

-- n - m
-- Alumno tiene varios cursos
-- Curso tiene varios alumnos
-- Al tener una relacion de muchos a muchos la FK no puede existir en alguna de las tablas y por ende se crea
-- una tabla Intermedia, Pivote, Puente en la cual en esa tablan iran las FK de las dos tablas (fk_alumno, fk_curso)

					CREATE DATABASE directorio;

CREATE TABLE usuarios (
	id SERIAL PRIMARY KEY,
	nombre TEXT,
	correo TEXT UNIQUE
);
-- Si ya ejecutaron la creacion de la tabla direcciones eliminenla con el DROP
--DROP TABLE direcciones;
CREATE TABLE direcciones (
	id SERIAL PRIMARY KEY,
	calle TEXT NOT NULL,
	numero TEXT,
	referencia TEXT,
	distrito TEXT,
	-- Si la columna que sera utiliza para la relacion es UNIQUE entonces es una relacion de 1-1 sino 1-n
	usuario_id INT, -- Es una columna corriente la relacion se crea en la linea de abajo
	
	-- ASI SE AGREGAR LA LLAVE FORANEA EN UNA RELACION DE 1-n
	CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

----------------------------------
-- Muchos a muchos
CREATE TABLE alumnos(
	id SERIAL PRIMARY KEY,
	nombre TEXT
);

CREATE TABLE cursos(
	id SERIAL PRIMARY KEY,
	nombre TEXT
);

CREATE TABLE alumnos_cursos(
	alumno_id INT,
	curso_id INT,
	CONSTRAINT fk_alumno FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
	CONSTRAINT fk_curso FOREIGN KEY (curso_id) REFERENCES cursos(id),
	-- Al ser una tabla Puente | Pivote
	PRIMARY KEY (alumno_id, curso_id)
);












