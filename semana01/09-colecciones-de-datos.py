# Listas (Arreglos)
# Coleccion de datos ordenada y editable
frutas = ['manzana', 'pera', 'kiwi', 'platano', 1, True]

# ordenada (la posicion empieza desde el 0)
print(frutas[0])

# se puede recorrer las listas tanto de izq a der como viceversa
print(frutas[-1])

# puedo sacar una sub-lista
print(frutas[1:3])

# Si no se le pone posicion inicial agarrara desde el comienzo
print(frutas[:3])

print(frutas[3:])

# Los metodos mas usados de las listas
# agregamos nuevos elementos al final de la lista
frutas.append('sandia')

# inserta el elemento en la posicion deseada
frutas.insert(1,'mango')
print(frutas)

# remove elimina el valor si lo encuentra y si no hay lanzara un error
frutas.remove(1)

# pop elimina el contenido por su indice y devulve el valor eliminado
eliminado = frutas.pop(5)
print(eliminado)
# opcionalmente el pop si no le pasamos el indice eliminara el ultimo elemento de la lista

# Ordena alfabeticamente los elementos de la lista, solamente funciona si todos los elementos de la lista son string
frutas.sort()
print(frutas)

# Reverse invierte el orden actual
frutas.reverse()
print(frutas)

# len devuelve la cantidad de elementos que hay en la lista
longitud =len(frutas)
print(longitud)

# Clear limpia toda la lista y la deja vacia
frutas.clear()
print(frutas)