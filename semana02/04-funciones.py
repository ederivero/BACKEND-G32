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

# podemos pasar parametros sin indicar el tipo de dato, PERO en las ultimas versiones se puede indicar el tipo pero no es restringido
# TIPADO > indicar el tipo de dato que debe ser la variable o parametro
def saludo_personalizado(nombre: str): 
    """Funcion que sirve para devolver un saludo en base al nombre"""
    # DOCUMENTACION DE LAS FUNCIONES
    return f"Bienvenido {nombre}"

print(saludo_personalizado("EDUARDO"))

def presentacion(nombre:str, edad:int, ciudad:str):
    return f"Hola me llamo {nombre}, tengo {edad} años y soy de {ciudad}"

# El orden que le pongamos a los parametros IMPORTA
print(presentacion("Juan", 23, "Tarapoto"))
print(presentacion("Roxana", 29, "Jaen"))
print(presentacion("Eduardo", 36, "Omate"))

# Si queremos modificar el orden de los parametros
print(presentacion(ciudad="Trujillo", nombre="Victor", edad=21))

def sumar(num1,num2):
    # Si en una funcion se manda a llamar al print pero no se retorna nada, se imprimira en la terminal pero no habra nada que retornar
    print(num1 + num2)

resultado = sumar(10,5)
print(resultado)


# Ejercicios
# 1. Crear una funcion calcular_area_rectangulo(base, altura) e imprima el resultado (base x altura)
def calcular_area_rectangulo(base: float, altura: float):
    resultado = base * altura
    print(f"El area del rectangulo es {resultado}")

calcular_area_rectangulo(10,2)
calcular_area_rectangulo(20,4)
calcular_area_rectangulo(15,7)

# 2. Crear una funcion es_par(numero) y que retorne si es par o impar (usando el %) (usemos OPERADOR TERNARIO)
def es_par(numero:int):
    return f"El {numero} es par" if numero % 2 == 0 else f"El {numero} es impar"

print(es_par(10))
print(es_par(15))
print(es_par(18))



# 3. Dado una lista de diccionarios de productos crear una funcion mostrar_info(producto) y que retorne el string "Hay {stock} unidades del producto {nombre}"
productos = [
    {
        "nombre":"Tomatodo 500ml", 
        "stock": 20
    }, 
    {
        "nombre":"Ventilador", 
        "stock": 50
    }, 
    {
        "nombre":"Parlante Bluetooth", 
        "stock": "25"
    }, 
    {
        "nombre":"Cafe en grano 500gr", 
        "stock": 100
    },
    {
        "nombree":"Cafe en grano 500gr", 
        "stock": 100
    }]

# Pasando producto por producto a la funcion
def mostrar_info(producto):
    return f"Hay {producto.get("stock")} unidades del producto {producto.get("nombre")}"

for producto in productos:
    print(mostrar_info(producto))

# Pasando todos los productos a la funcion e internamente los iteramos
def mostrar_info_todos(productos):
    for producto in productos:
        print(f"Hay {producto.get("stock")} unidades del producto {producto.get("nombre")}")

mostrar_info_todos(productos)

print('------------')
# Se necesita buscar en la lista de productos el stock de determinado producto, si no lo encuentra indicar que el producto no existe
def mostrar_stock_producto(nombre):
    for producto in productos:
        if producto.get("nombre") == nombre:
            return f"Hay {producto.get("stock")} unidades"
         
    return "El producto no existe"

nombre = input("Ingresa el nombre del producto a buscar: ")
print(mostrar_stock_producto(nombre))

