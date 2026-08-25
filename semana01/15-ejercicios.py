# 1. Dado la lista numeros = [4,8,15,16,23,42] Usando un for calcula la suma total
numeros = [4,8,15,16,23,42]
total = 0
for numero in numeros:
    # total = total + numero
    total += numero

print(f"El total de la suma es: {total}")

# 2. Dado la lista de nombres = ["Joshua", "Judith", "Eduardo","Jean Pierre", "Luis"] quiero convertir todos los nombres a mayuscula (.upper())

nombres = ["Joshua", "Judith", "Eduardo","Jean Pierre", "Luis"]
nombres_mayusculas = []

# print("Los nombres en mayuscula son:", end=' ')
for nombre in nombres:
    # print(nombre.upper(),end=',')
    nombres_mayusculas.append(nombre.upper())

# Usando el end y el join
print("Los nombres en mayuscula son:",end=' ')
print(",".join(nombres_mayusculas))

# De la manera facil y rapida
print(f"Los nombres en mayuscula son: {nombres_mayusculas}")

# 3. Dado la lista de precios = [10.5, 14.8, 17.2, 19.45] Calcular el promedio y la cantidad de elementos de la lista
precios = [10.5, 14.8, 17.2, 19.45]
# total = len(precios)
total = 0
promedio = 0
suma = 0

for precio in precios:
    suma += precio

    # Incrementador
    total += 1
promedio = suma / total
# Si una variable flotante queremos limitar sus decimales usamos :.nf
print(f"El total de elementos de la lista es {suma} y su promedio es {promedio:.2f}")


# 4. Tengo la siguiente lista de tuplas estudiantes = [("Juana", 26), ("David", 30), ("Ronaldo",18), ("Fatima", 23)] usando un for desempaquete la tupla e imprime usando el formato "NOMBRE tiene EDAD años"
estudiantes = [("Juana", 26), ("David", 30), ("Ronaldo",18), ("Fatima", 23)]

for estudiante in estudiantes:
    print(f"{estudiante[0]} tiene {estudiante[1]} años")

# Destructuracion de la tupla
for nombre,edad in estudiantes:
    print(f"{nombre} tiene {edad} años")

# 5. Tengo el diccionario
producto = {
    "nombre":"Tarjeta Grafica",
    "precio":3020.52,
    "especificaciones":"Tarjeta grafica de ultima generacion",
    "pros":["Economica","Moderna","Sencilla instalacion"],
    "contras": ["No hay garantia", "Se sobrecalienta","No tiene drivers"],
    "info_adicional":{
        "pais_procedencia":"China",
        "estado":"Nuevo",
        "caja":False
    }
} 
# Necesito saber cuantos pros tengo y cuantos contras tengo, asi mismo quiero saber que pais_procedencia es y cual es el ultimo contras
print(len(producto["pros"]))
print(", ".join(producto["pros"])) # si quiero mostrar los elementos de una lista o tupla y evitar mostrar los [] o () usamos el join, asi mismo, esto convierte la coleccion de datos a un string
print(len(producto["contras"]))
print(producto["info_adicional"]["pais_procedencia"])
print(producto["contras"][-1])

# 6. Tengo una lista de tuplas ventas = [("enero", 1500), ("febrero", 2300), ("marzo",1800)] recorrela en un for y construye un diccionario ventas_dic donde la clave sea el mes y el valor sea el monto. Es decir, el resultado final debe ser 
# ventas_dic = {"enero":1500, "febrero":2300, "marzo":1800}
ventas = [("enero", 1500), ("febrero", 2300), ("marzo",1800)]
ventas_dic = {}

for mes, monto in ventas:
    ventas_dic[mes] = monto

print(ventas_dic)

# .items() devuelve los elementos del diccionario en una tupla en la cual la primera posicion es la llave y la segunda es el valor y por ende se hace una destructuracion
for llave,valor in ventas_dic.items():
    print(f"{llave}:{valor}")