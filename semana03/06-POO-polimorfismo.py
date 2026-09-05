# Polimorfismo > Poli (muchas) morfo (formas) muchas formas de poder tener el mismo metodo pero con diferente resultado, esto va a depende de la clase donde se encuentre

class Animal:
    def hacer_sonido(self):
        print("Este animal hace un sonido")

    def existir(self):
        print("Yo existo")

class Perro(Animal):
    def hacer_sonido(self):
        # Si queremos reutilizar el contenido del metodo padre lo llamamos usando super()
        super().existir()
        super().hacer_sonido()
        print("Guau guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau miau")

class Vaca(Animal):
    def hacer_sonido(self):
        print("Muuu")


# lista de instancias
animales = [ Perro(), Gato(), Vaca()]

for animal in animales:
    # el mismo metodo tiene diferente resultado (forma)
    animal.hacer_sonido()
    animal.hacer_sonido()

# El polimorfismo sirve para escribir codigo mas generico indicando que siempre voy a tener ese metodo porque esta "dentro de la familia" y no voy a tener que validar que el metodo existe antes de llamarlo sea cual sea la clase
# Es la base de muchos patrones de diseño y de las librerias como Django Flask
