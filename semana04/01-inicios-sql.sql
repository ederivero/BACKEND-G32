-- En el archivo sql solo se ejecutaran las lineas que no empiecen con --
-- Asimismo en SQL (Structured Query Language) SIEMPRE debe terminar la instruccion con ;
-- Cuando en la terminal aparece un `=` luego de el nombre de usuario del servidor esto significa que esta esperando una nueva consulta
-- Cuando aparece un `-` significa que ya hemos empezado una consulta y esta esperando o mas indicaciones o la finalizacion
-- Cuando aparece una `'` o `"` significa que he abierto una pero aun no la he cerrado
-- en SQL NO ES LO MISMO comilla simple que COMILLA DOBLE, la comilla simple se usa para texto, es decir para mostrar o almacenar texto MIENTRAS que la comilla doble se usa para llamar a nombre de tablas, columnas y nombre reservados

-- Tenemos dos sub conjuntos de lenguajes 
-- DDL : Data Definition Language (Lenguaje de definicion de datos)

-- CREATE: Crear entidades (BASES DE DATOS, TABLAS, USUARIOS, COLUMNAS, TRIGGER)
-- ALTER: Alterar (modifica) tablas, bases de datos, usuarios, etc
-- DROP: Eliminar entidades (tabla, bd, etc)
-- TRUNCATE: Elimina la data dentro de la tabla sin eliminar la tabla
-- RENAME: Cambiar el nombre de las entidades

CREATE DATABASE pruebas;

-- Cuando utilizamos un comando de psql no estamos obligados a poner ;, es opcional
\c pruebas


-- Sirve para ejecutar cualquier comando de la terminal fuera de postgres
-- Limpiaremos la termina
\! clear
\! cls

CREATE TABLE personas (
    -- Ahora definimos las columnas
    -- nombre_columna tipo_de_dato opciones_adicionales
    id SERIAL PRIMARY KEY,  -- Solamente puede existe una columna SERIAL en toda la tabla
    -- UNIQUE > Indica que un registro no pueda tener el mismo valor de otro registro en esa columna
    -- NOT NULL > Indica que la columna jamas podra tener valores nulos
    -- NULL > Si podra tener valores nulos (config por defecto)
    -- PRIMARY KEY > Indica que la columna sera escogida como representacion del registro y se usara para encontrar el registro mas rapido, aca generalmente suelen ser los ID's
    -- DEFAULT valor > Indica que al momento de registrar o actualizar el valor de la columna si no se ingresa nada se podra el valor como valor predeterminada 
    nombre TEXT NOT NULL, -- TEXT No tiene limites, es decir podemos almacenar grandes cantidades de texto y este variara su almacenamiento en base al texto almacenado
    apellido VARCHAR(50),
    correo TEXT NOT NULL UNIQUE,
    fecha_nacimiento TIMESTAMP WITH TIME ZONE
);

-- Para ver las tablas creadas en la bd
\dt


-- Para ver las tablas y las secuenciales (autoincrementables) creadas en la base de datos
\d


-- Nos mostrara la definicion de toda la configuracion de esa tabla
\d NOMBRE_TABLA