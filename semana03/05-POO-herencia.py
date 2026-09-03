class Empleado:
    def __init__(self,nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def mostrar_info(self):
        print(f"{self.nombre} gana {self.sueldo}")

# Heredo mi clase
class EmpleadoVentas(Empleado):
    pass

# Al heredar de una clase jalaremos toda su configuracion (metodos y atributos publicos y protegidos)
vendedor = EmpleadoVentas("Roxana",2000)
vendedor.mostrar_info()

# Clase padre / superclase > La clase original (Empleado)
# Clase hija / subclase > La clase que hereda (EmpleadoVentas)
# Herencia > La hija obtiene automaticamente atributos y metodos del padre

class EmpleadoMkt(Empleado):
    def __init__(self, nombre, sueldo, comision):
        # cuando queremos reutilizar el mismo metodo de la clase padre usamos super()
        super().__init__(nombre, sueldo)
        self.comision = comision

###################################################
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} esta comiendo :P")

    def dormir(self):
        print(f"{self.nombre} esta durmiendo zzz")


class Gato(Animal):
    # si queremos sobre-escribir algun metodo del padre
    def __init__(self, nombre, edad):
        self.edad = edad
        super().__init__(nombre)

    def araniar(self):
        print(f"{self.nombre} esta arañando ")

    def dormir(self):
        # Si no mandamos a llamar al metodo del padre (super()) estaremos SOBREESCRIBIENDO el comportamiento del metodo en el hijo
        print(f"{self.nombre} esta en el techo durmiendo sabroso")


class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} esta ladrando")

    def comer(self):
        super().comer()
        print(f"Esta comiendo feliz!")

g = Gato("Michi","15 meses")
p = Perro("Chiwi")
g.comer()
g.araniar()
g.dormir()

p.dormir()
p.ladrar()
p.comer()


# Crear una clase padre llamada Figura y dos clases hijos llamada Cuadrado y Triangulo. La clase Figura tiene el atributo  nombre y un metodo area() que retorna 0 por defecto. La clase Cuadrado tiene un atributo adicional lado y la clase Triangulo tiene atributo base y altura, ambas clases heredan de Figura y se necesita sobreescribir el metodo area()
class Figura:
    def __init__(self,nombre):
        self.nombre = nombre

    def area():
        return 0

class Cuadrado(Figura):
    def __init__(self, nombre, lado):
        super().__init__(nombre)
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Triangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base 
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

# Clase Persona y clase Guerrero y Mago en la cual Persona tiene nombre y vida (valor predeterminado es 100) y un metodo recibir_danio(cantidad) que resta vida hasta llegar a 0. Guerrero tiene el atributo fuerza y un metodo atacar() que imprime el daño causado segun la fuerza. La clase Mago tiene atributo mana y un metodo lanza_hechizo() que solo funciona si tiene suficiente mana (sino muestra un mensaje de error)
class Persona:
    def __init__(self, nombre, vida = 100):
        self.nombre = nombre
        self.vida = vida

    def recibir_danio(self, cantidad):
        if self.vida - cantidad < 0:
            return "Ya se murio" 
        
        self.vida -= cantidad

class Guerrero(Persona):
    def __init__(self, nombre, fuerza, vida=100):
        super().__init__(nombre,vida)
        self.fuerza = fuerza

    def atacar(self):
        return f"Has hecho {self.fuerza} puntos de daño"
    

class Mago(Persona):
    def __init__(self, nombre, mana, vida=100):
            super().__init__(nombre,vida)
            self.mana = mana

    def lanza_hechizo(self, costo_de_mana):
        if costo_de_mana > self.mana:
            return "No se puede lanzar el hechizo por falta de mana!"

        return "Lanzando el hechizo!"


persona = Persona("Anakin", 80)
print(persona.recibir_danio(110))

persa = Guerrero("Leonidas",100)
print(persa.atacar())

merlin = Mago("Merlin",50,70)
merlin.recibir_danio(20)
print(merlin.lanza_hechizo(100))
print(merlin.lanza_hechizo(40))