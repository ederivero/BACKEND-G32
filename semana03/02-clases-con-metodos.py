# Las clases SIEMPRE empiezan con Mayuscula
class Mueble:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo

    def dimensiones(self):
        print(f"""Las dimensiones son: 
Largo: {self.largo}
Ancho: {self.ancho}
Alto: {self.alto}""")

m1 = Mueble(1.4, 0.7, 1.2)
m1.dimensiones()
# Si se quiere cambiar los valores ingresados al inicio
m1.largo = 1.8
m1.dimensiones()

# Si no se le pasa el self como primer parametro, ese metodo solo podra ser accedido directo desde la clase, es decir, sin instancia
# Mueble.dimensiones()

# 1. Crear una clase Rectangulo en la cual tengamos en el constructor la base y la altura y tener un metodo para calcular su area calcular_area en la cual retorne el area (base x altura)

# 2. Crear una clase Estudiante en la cual tenga el atributo nombre, notas, correo que deben ser inicializados el nombre y el correo y tenga su metodo agregar_nota(nota), tambien su metodo promedio() que me de el promedio de todas las notas y el metodo estado que me su estado si esta Aprobado (>=13), Subsa (11 - 12) o Jalado (0-10)
# Se puede utilizar una llamada a un metodo dentro de otro (algo asi como llamar a una funcion dentro de otra)