# Scope (Alcance) como puedo utilizar mis variables dentro de las funciones

def calcular():
    resultado = 100
    print(resultado)

calcular()
# La variable resultado solo existe dentro de la funcion
# print(resultado)

# Las variables globales (no estan dentro de la funcion) si pueden ser leidas dentro de la funcion
nombre = "Eduardo"

def mostrar():
    # Si "modificamos" una variable global, no se modificara, sino lo que se hara se creara otra variable local dentro de la funcion con el mismo nombre pero en una posicion de memoria diferente
    nombre = "Juanito"
    # la funcion id es una funcion de Python que sirve para retornar el identificador unico de esa variable
    print(id(nombre))
    print(nombre)

mostrar()   
print(id(nombre))
print(nombre)

contador = 0

# def incrementar():
#     # como modificamos la variable entonces se crea una nueva, pero al incrementar en 1 el valor inicial no existe
#     contador += 1

# incrementar()

# NO HAY QUE ABUSAR DE ESTO! (Es una mala practica porque podemos malograr el ciclo de la variable (alterar su resultado sin que nos demos cuenta))
def incrementar():
    # al quere utilizar una variable global para modificarla dentro de la funcion usamos la palabra reservada global
    global contador 
    contador += 1

incrementar()
incrementar()
incrementar()

print(contador)

# La forma correcta de evitar el uso de "global"
contador = 0
def incrementar_en_uno(valor):
    return valor + 1

contador = incrementar_en_uno(contador)
contador = incrementar_en_uno(contador)
contador = incrementar_en_uno(contador)
contador = incrementar_en_uno(contador)
print(contador)