# String (texto)
# Se identifican por tener comilla simple o doble
# Se puede crear strings pero de varias lineas usando la tiple (doble) comilla 
nombre = 'Eduardo O\'Conner'
print(nombre)
nombre = "Eduardo O'Conner"

# al poner el caracter 'r' al comienzo del string este interpretara el uso del back-slash como un caracter mas y no para poder hacer uso de caracteres especiales
ruta = r'C:\documents\etc'
print(ruta)
texto = '''Hola soy su profesor.
El dia de hoy continuaremos avanzando con Python.
    Hoy haremos varios ejercicios'''

apellido = "De Rivero"

persona = 'Eduardo'
# el prefijo f lo que hace es que lo que ponga entre {} podra ser codigo python
saludo = f'Hola {persona}, mucho gusto'
print(saludo)
# Si no quieres usar el prefijo f
# para el uso del metodo format la misma cantidad de llaves tiene que haber con la misma cantidad de parametros
saludo = 'Hola {}, mucho gusto'.format(persona)
print(saludo)

# Enteros o Int
edad = 30

# Decimales o Float
estatura = 1.88

# Boolean 
aprobado = True 
viudo = False

# Las variables en python nunca pueden empezar con numeros, tampoco con caracteres especiales\
# no se recomienda empezar con _ porque puede malentederse con encapsulamiento de POO

# Para saber el tipo de variable se usa la funcion type
print(type(saludo))

