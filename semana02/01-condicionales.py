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


# Se necesita registrar la venta por teclado y si la venta es mayor o igual a 100 soles entonces agregar un descuento del 10%, caso contrario no agregar descuento y luego mostrar cuanto debe de pagar.
venta = float(input("Ingrese el monto: "))
monto_a_pagar = 0
if venta >= 100:
    monto_a_pagar = venta * 0.9
    # es lo mismo que esto
    # descuento = 0.10
    # monto = venta - venta * descuento
else:
    monto_a_pagar = venta

print(f"El monto a pagar es: {monto_a_pagar}")

# OPERADOR TERNARIO
# se usa si en el if-else solo vamos a tener una sola linea de codigo

# variable =  RESULTADO_SI_ES_VERDADERA if CONDICION else RESULTADO_SI_NO_ES_VERDADERA
monto_a_pagar = venta * 0.9 if venta >= 100 else venta
print(f"El monto a pagar es: {monto_a_pagar}")

# ESTO ES EN JAVASCRIPT: CONDICION ? RESULTADO_SI_ES_VERDADERA : RESULTADO_SI_NO_ES_VERDADERA 


# Usando el operador ternario indiqueme si el numero es "Par" o "Impar"
numero = 11
#    RESULTADO_SI_SE_CUMPLE if CONDICION       else RESULTADO_SI_NO_SE_CUMPLE
resultado = "Par"           if numero % 2 == 0 else "Impar"

print(f"El numero {numero} es {resultado}")


# if anidados
# si su nota es entre 90 y 100 es excelente, si su nota es entre 70 y 90 es bueno, si su nota es entre 50 y 70 es regular y si es menor que 50 es malo
nota = 15

if nota >= 90 and nota <= 100:
    print("Es excelente")
# si no, entonces si… | sino pero si cumple la condicion
elif nota >= 70:
    print("Es bueno")
elif nota >= 50:
    print("Es regular")
else:
    print("Es malo")


nacionalidad = ""

if nacionalidad == "PERUANO":
    print("Que rico es el ceviche")
elif nacionalidad == "BOLIVIANO":
    print("Que rico es la salteña")
elif nacionalidad == "COLOMBIANO":
    print("Que rico es la bandeja paisa")


# PARA CUANDO TE HACEN VARIAS CONDICIONES
# SWITCH - CASE 

# En base al numero del dia de la semana si es 1, es lunes, si es 2, es martes, si es 3 , es miercoles y asi sucesivamente
numero = 1
dia = "" 
if numero == 1:
    dia = "Lunes"
elif numero == 2:
    dia = "Martes"
elif numero == 3:
    dia = "Miercoles"
# ...


# Crear una calculadora simple en la cual vamos a ingresar el numero1 , operacion que puede ser "+" (Suma), "-" (Resta), "*" (Multiplicacion), "/" (Division), numero2, retornar el resultado
# Utilizar if y elif para la operacion, asi mismo, si se ingresa una operacion diferente retornar un mensaje que diga "INCORRECTO"

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
operacion  = input("Ingrese la operacion: ")

resultado = ''

if operacion == "+":
    resultado = numero1 + numero2

elif operacion == "-":
    resultado = numero1 - numero2

elif operacion == "*":
    resultado = numero1 * numero2

elif operacion == "/":
    if numero2 == 0:
        resultado = "No se puede dividir entre 0"
    else:
        resultado = numero1 / numero2
else:
    resultado = "INCORRECTO"

print(resultado)