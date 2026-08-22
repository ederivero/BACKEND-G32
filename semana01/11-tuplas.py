# Coleccion de datos que es ordenada pero NO es editable
# Una vez que se crea ya no se puede modificar

persona = ("Eduardo", 30, "Arequipa")

print(persona[0])

# No se puede ni modificar el contenido de las posiciones
# persona[0]='Ramoncito'

# Desempaquetar los datos en variables independientes
nombre, edad, ciudad = persona
nombre = 'Ramoncito'
edad = persona[1]

print(persona)

# CUIDADO AL CREAR LAS TUPLAS DE UN SOLO ELEMENTO
numeros = (1)
# Cuando yo creo una tupla de un solo elemento y este no tiene una coma al final, los parentesis representantes de la tupla no son considerados y al final se eliminan
print(type(numeros))

# Para crear la tupla de un solo elemento
numeros = (1,)
print(type(numeros))
