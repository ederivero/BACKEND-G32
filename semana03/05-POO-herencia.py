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