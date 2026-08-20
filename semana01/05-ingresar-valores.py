nombre = input('Ingresa tu nombre: ')

print(f'Tu nombre es {nombre}')

# todo lo que se ingresa por el input SIEMPRE es string 
# en Python para convertir de un tipo de dato a otro solo se necesita invocar al tipo de dato que queremos usar
edad = '34'
# Asi se convierte a un int 
edad_numerica = int(edad)
# NOTA: No se puede convertir cualquier cosa, hay que tener COHERENCIA
# edad_numerica = int('Treinta y cuatro')