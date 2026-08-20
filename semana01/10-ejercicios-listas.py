# 1. Crear una lista de 5 productos, luego, agregar uno nuevo, eliminar el 2do producto y ordenar alfabeticamente los productos e imprimirlos
productos = ['pan','mantequilla','mermelada','manjar','aceituna']

# agregar uno nuevo
productos.append('mantequilla de mani')

# eliminar el 2do
productos.pop(1)

# ordenar alfabeticamente
productos.sort()

print(productos)

# 2. tengo la siguiente lista (matriz)
matriz = [[1,2],[3,4]]
# Como hago para obtener el '3'
print(matriz[1][0])