-- Funciones de agregacion 
-- Aggregate functions sirve para poder tener un poco de logica en nuestras consultas

-- GROUP BY Al usar GROUP BY se tiene que agrupar todas las columnas que se seleccion
SELECT categoria FROM productos
-- WHERE
GROUP BY categoria;

-- https://www.postgresql.org/docs/9.5/functions-aggregate.html

-- COUNT > Contar
SELECT activo, COUNT(activo) 
FROM productos
GROUP BY activo;

-- SUM > Sumar
-- Visualizar los stocks de las categorias activos
SELECT categoria, SUM(stock)
FROM productos
WHERE activo = true
GROUP BY categoria;


-- AVG > Promedio
-- Promedio de los precios por categoria
SELECT categoria, AVG(precio) 
FROM productos
GROUP BY categoria;


-- MIN / MAX > Devuelve los valores MIN o MAX
-- Quiero los valores maximos de los precios por categoria pero que solo sean activos
--SELECT MAX(precio) ...
SELECT categoria, MAX(precio)
FROM productos
WHERE activo = TRUE 
GROUP BY categoria;


-- Si queremos usar una funcion de agregacion para condicionales entonces usamos la clausula HAVING
SELECT categoria, SUM(stock)
FROM productos
WHERE activo = TRUE
GROUP BY categoria
HAVING SUM(stock) > 40;

-- Si quiero modificar el orden de visualizacion de mis resultados usamos el ORDER BY
SELECT categoria, SUM(stock)
FROM productos
WHERE activo = TRUE 
GROUP BY categoria, activo
HAVING SUM(stock) >= 40 AND AVG(precio) BETWEEN 10 AND 50
ORDER BY sum(stock) DESC, categoria DESC;

-- ASC > 0 - 9 | A -Z 
-- DESC > 9 - 0 | Z - A

-- SELECT 
-- FROM
-- WHERE
-- GROUP BY
-- HAVING
-- ORDER BY


