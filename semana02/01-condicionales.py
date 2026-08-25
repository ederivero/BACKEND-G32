edad = 10

# si ingresa al if ya no ingresa al else y solo ingresara al else si nunca ingreso al if
if edad >= 18:
    print("Puedes ingresar a la pagina")
# tambien se puede agregar un escenario en el cual no se cumpla la condicion
else:
    print("Ve a google")

# Lo que se coloque fuera del bloque de identacion siempre se va a ejecutar
print("Gracias por usar el programa")



# Pedir un numero por teclado, convertir ese numero a int y ver si el numero es positivo SOLO SI ES MAYOR que 0
# int > integer (entero)
# float > flotante
numero = int(input("Ingresa un numero por teclado: "))

if numero > 0:
    print("Es positivo")
else:
    print("Es negativo")