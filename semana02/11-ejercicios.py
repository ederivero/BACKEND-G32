# 1. Crea una funcion calcular_igv en la cual pide el precio y retorne el precio final aplicado el igv (18%) - puede utilizar lambda
def calcular_igv(precio):
    precio_con_igv= precio * 1.18
    return precio_con_igv

#  Ahora con lambda
calcular_igv_lambda = lambda precio: precio * 1.18

# print(calcular_igv(100))
# print(calcular_igv_lambda(100))

# 2. Convierte la temperatura en la funcion cambiar_temperatura de Celcius a Farenheit - puede utilizar lambda
def cambiar_temperatura(celcius):
    return (celcius * 9/5) + 32

cambiar_temperatura_lambda = lambda celcius: (celcius * 9/5) + 32

# print(f"{cambiar_temperatura(100)} F")
# print(f"{cambiar_temperatura_lambda(100)} F")

# 3. Dado un diccionario de un producto (nombre, precio, stock) utiliza if-elif-else para clasificar el stock en "Sin Stock" (si el stock es 0), "Stock Bajo" (si el stock es entre 1 y 10) y "Disponible"(si el stock es mas que 10)
def clasificar_stock(producto):
    stock = producto.get("stock")

    if stock == 0:
        estado = "Sin Stock"
    elif 1 <= stock <= 10: # 1 <= stock and stock <= 10
        estado = "Stock Bajo" 
    else: 
        estado = "Disponible"
    print(f"El producto {producto.get("nombre")} tiene un estado de {estado}")

producto = {"nombre": "Ayudin", "precio": 4.5, "stock": 5}
# clasificar_stock(producto)

# 4. Usando un while, simula un cajero automatico simple que pida una clave hasta que el usuario la ingrese correctamente, usando 3 intentos como maximo, sino indica que la cuenta fue bloqueada.
def cajero_automatico():
    clave_correcta = "4591"
    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        clave_ingresada = input("Ingresa tu clave: ")

        if clave_ingresada == clave_correcta:
            print("Bienvenido")
            break
        else:
            intentos += 1
            if intentos < max_intentos:
                print(f"Clave incorrecta. Te quedan {max_intentos - intentos} intentos.")
    else:
        # Solamente vamos a ingresar al else si el while termino sin un break
        print("Cuenta bloqueada por exceder el numero de intentos")

# cajero_automatico()
# 5. Crear una funcion calcular_area_circulo(radio) que retorne el area (3.1415 como valor de pi) - puede utilizar lambda
# pi * radio ** 2
pi = 3.1415
calcular_area_circulo = lambda radio: pi * (radio ** 2)
# print(f"{calcular_area_circulo(10):.1f}") 
# print(f"{80.28274728974673874638763846378:.1f}") 

# 6. Crear una funcion procesar_notas(nombre, *notas) que calcule y retorne el promedio y luego clasifique el resultado con if-elif-else en una segunda funcion clasificar(promedio)

def clasificar(promedio):
    if promedio < 11:
        return "Desaprobado"
    elif 11<= promedio <14:
        return "Regular"
    elif 14 <= promedio < 17:
        return "Bueno"
    else:
        return "Excelente"

def procesar_notas(nombre, *notas):
    if len(notas) == 0:
        print(f"{nombre} no tiene notas registradas")
        return 

    promedio = sum(notas) / len(notas)
    resultado = clasificar(promedio)
    print(f"{nombre} esta {resultado}")

# procesar_notas("Eduardo", 15,10,13,5)
# procesar_notas("Karina", 10,20,10)
# procesar_notas("Ruben", 18)

# 7. En una lista de 5 elementos crear una funcion obtener_por_indice(lista, indice) que capture el error IndexError si el indice no existe

def obtener_por_indice(lista, indice):
    try: 
        print(lista[indice])
    except IndexError:
        # el IndexError se emite cuando se quiere acceder a una posicion invalida de una lista, tupla
        print(f"Error: El indice {indice} no existe!")
        return


# obtener_por_indice([10,20,30],0)
# obtener_por_indice(("a","e","i"), 2)
# obtener_por_indice([1,2,3], 5)

# BONUS!
# 8. Crear una funcion con while True que pida numeros al usuario y los sume manejando un try-except en el que caso que se ingrese un texto en vez de numeros y que al escribir Salir, termine la sumatoria sin lanzar el error
def sumatoria_infinita():
    suma = 0

    while True:
        entrada = input("Ingresa un numero, o Salir para terminar: ")
        if entrada.lower() == "salir":
            print(f"Fin, la suma es {suma}")
            break

        try:
            numero = float(entrada)
            suma += numero
        except ValueError:
            # ValueError se da al momento de querer convertir un texto a numero
            print("Entrada invalida, por favor ingresa un numero o sino escribe Salir")

sumatoria_infinita()