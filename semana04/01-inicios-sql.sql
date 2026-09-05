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