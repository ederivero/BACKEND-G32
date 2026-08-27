# Una funcion es un bloque de codigo que se puede repetir las veces que sea necesario
# def > definition
def saludar():
    print("Hola soy una funcion")

# Declara la funcion: definir su funcionamiento

# Invocar a la funcion: llamar para ejecutar su contenido
saludar()

# Si en mis funciones aun no tengo la logica definida puedo usar pass, esto tambien sirve para los bloques de codigo como if-else, for, while
def calcular_promedio():
    pass # no hace absolutamente nada y una vez que se ponga codigo se debe quitar

calcular_promedio()
# en python se recomienda usar tanto en funciones como en nombre de variables el snake_case 
# 3 tipos de convencion de escribir: snake_case, CamelCase, pascalCase 


# pueden retornar informacion
def obtener_tipo_cambio():
    # supongamos que consumimos una API
    dolar_compra = 3.31
    dolar_venta = 3.48
    return {"dolar_compra": dolar_compra, "dolar_venta": dolar_venta} # Luego de poner la palabra return no podemos escribir mas codigo dentro de la funcion

resultado = obtener_tipo_cambio()
resultado2 = obtener_tipo_cambio()

print(resultado)