# Tenemos un numero que adivinar entonces pedir al usuario que ingrese un numero entre el 1 y el 20 hasta que lo adivine, una vez que lo adivine indicale "GANASTEEE" y terminal el while, use break
secreto = 10

# la condicion siempre va a ser Verdadera (bucle infinito)
# while True:
#     pass

# no_adivino =True
# while no_adivino:
#     numero = int(input("Ingresa un numero entre 1 y 20: "))
#     if numero == secreto:
#         print("GANASTESS!!!")
#         no_adivino = False
#     else:
#         print("Sigue intentando")

while True:
    numero = int(input("Ingresa un numero entre 1 y 20: "))
    if numero == secreto:
        print("GANASTESS!!!")
        break
    else:
        print("Sigue intentando")
    print("BUUUUU!!")


# Ingresar 5 precios a la lista y si se ingresa un valor negativo o 0 no se debe de tomar en consideracion
lista_precios = []
# NO USAR BREAK, SOLO CONTINUE
while len(lista_precios) < 5:
    precio = int(input("Ingresa el precio: "))

    if precio <= 0:
        print("El precio no puede ser negativo")
        continue
    lista_precios.append(precio)

print("Gracias por ingresar los precios")
print(lista_precios)