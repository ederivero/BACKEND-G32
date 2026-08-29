# en python tenemos la posibilidad de crear funciones de una sola linea y esta se conocen como funciones lambda
# Automaticamente retorna el resultado de la operacion
sumar = lambda num1, num2: num1+num2 if num1 > 10 else num1*num2

def sumar(num1,num2):
    if num1 > 10:
        return num1 + num2
    else:
        return num1 * num2

resultado = sumar(10,20)
print(resultado)

# Necesito una funcion es_correo que verifique que el correo contiene un `@`` y un `.` usando lambda functions y ademas dentro de los str se puede usar la palabra `in` para ver si esta o no esta ese caracter
es_correo = lambda correo: "@" in correo and "." in correo
print(es_correo("ederiveromangmail.com"))
print(es_correo("ederiveroman@gmailcom"))
print(es_correo("ederiveroman@gmail.com"))


# Necesito una funcion generar_slug
# slug es convertir el texto "Bienvenidos a la Clase" a "bienvenidos-a-la-clase", es decir, convierte los espacios por guinos y lo pone todo en minuscula
# pueden usar la funcion .lower() y la funcion .replace()
# anidamiento de metodos
generar_slug = lambda texto : texto.lower().replace(" ","-")

print(generar_slug("Bienvenidos a la Clase"))