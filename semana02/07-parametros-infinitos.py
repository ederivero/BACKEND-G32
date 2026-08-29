# en el caso que nosotros recibiesemos una cantidad indeterminada de parametros usamos el *args (arguments)
def promedio_notas(*notas):
    # el parametro * es una tupla que nunca la voy a poder editar
    print(notas)
    # quiero sacar el promedio de todas las notas
    # Metodo 1: usando funcion sum
    # promedio = sum(notas) / len(notas)

    # Metodo 2: Usando for e incrementadores
    total = 0
    for nota in notas:
        total += nota
    promedio = total / len(notas)
    print(promedio)

# al pasarle los parametros seran con ,
promedio_notas(15,20,6,12,8.5)
promedio_notas(15,20,8.5)
promedio_notas(13,10)
promedio_notas(15,6,9)

# Se puede tambien combinar los parametros con los *args
# No se puede colocar otro parametro luego de los *args
# Para el tipado de una coleccion de datos si queremos indicar que todos los elementos van a ser int, entonces [int,...]
# si queremos indicar que la tupla va a tener SOLO 2 ELEMENTOS y esos van a ser int y str, entonces [int, str]
# tuple > tupla 
# dict > diccionario
# list > lista
# object > conjunto
def promedio_notas_alumno(nombre:str, *notas: int):
    print(nombre)
    print(notas)

promedio_notas_alumno("Eduardo",10,20,5)

