try: # intentalo
    numero = int(input("Ingresa un numero: "))
    print(numero * 10)
except: # excepcion (Si no lo intento bien)
    print("Numero invalido")

print("Yo aun sigo trabajando")


# Tambien se puede filtrar los errores segun su tipo
try:
    numero = int(input("Ingresa un numero: "))
    print(10 / numero )
# Generalmente se colocan los errores identificados
except ValueError:
    print("Numero invalido")
except ZeroDivisionError:
    print("No se puede dividir entre 0!")
# Y luego si por algun motivo se genera un error no registrado
except:
    print("Error desconocido!")
