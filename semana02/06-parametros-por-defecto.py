# Si al crear una funcion le colocamos su valor al parametro, entonces si al momento de llamar a la funcion no se le da ese parametro, usara el valor por defecto
def saludar(saludo="Buenas noches"):
    print(saludo)

saludar()
saludar("Holis")
saludar(saludo="Aloha")

# NOTA: Si queremos utilizar parametros y parametros con valor predeterminado, los parametros con valores predeterminados van al final
def registrar_alumno(nombre, curso="Backend"):
    print(f"El alumno {nombre} fue registrado al curso de {curso}")

registrar_alumno("Eduardo")
registrar_alumno("Martita","Frontend")

# 1. Crear una funcion calcular_dscto en la cual tendremos el parametro de precio y porcentaje , si no se da el porcentaje su valor debe ser 10, calcular el descuento de 3 productos, en los cuales dos de ellos no se les pase el parametro de porcentaje
def calcular_dscto(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    monto = precio - descuento
    print(f"El precio {precio} su descuento es de {descuento} y el monto final seria {monto}")

articulos = [{"monto": 500}, {"monto": 1200}, {"monto": 80, "tasa": 25}]
for articulo in articulos:
    # calcular_dscto(articulo.get("monto"), articulo.get("tasa")) if articulo.get("tasa") else calcular_dscto(articulo.get("monto"))
    if articulo.get("tasa"):
        calcular_dscto(articulo.get("monto"), articulo.get("tasa"))
    else:
        calcular_dscto(articulo.get("monto"))

# calcular_dscto(20)
# calcular_dscto(50)
# calcular_dscto(75,25)