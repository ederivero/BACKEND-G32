# For plano (sin el uso de ninguna coleccion de datos)
# range(x,y,z)
# Si solo utilizamos un parametro
# x > TOPE, es decir hasta que numero va a incrementar menor que desde 0
# y > INICIO, es decir desde que numero va a empezar
# z > MODIFICADOR, es decir de cuanto en cuanto se va a incrementar/decrementar, su valor por defecto es 1
# siempre cuando queremos que empiece el for le ponemos ":"
for numero in range(10):
    None  # Si aun no sabemos que hacer en este bloque de codigo podemos usar el None

# En python no se puede poner bloques de codigo tabulados si no estan precedidos por un estatuto de identacion (for)
print("hola")
print("uf, termine!")

for numero in range(5, 10):
    print(numero)

for numero in range(5, 10, 2):
    print(numero)

print("----------")
# Los for son mas utiles dentro de las colecciones de datos porque puedo iterar y navegar por cada uno de sus elementos
# Todas las colecciones de datos son iterables
numeros = [10, 15, 7, 20, 13, 9]

for x in numeros:
    print(x)
