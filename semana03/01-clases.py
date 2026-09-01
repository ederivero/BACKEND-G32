# Persona 
# ojos, orejas, brazos, cabello, dientes (ATRIBUTOS)
# caminar, correr, nadar, lanzar (METODOS)
# Clase tiene atributos y metodos

class Persona:
    nombre = ""
    edad = 0

# instancia > Crear una copia completa de toda la clase
# al momento de crear una instancia TODOS LOS ATRIBUTOS Y METODOS van a ser PROPIOS de esa variable 
p1 = Persona()
p2 = Persona()
print(type(p1))

# Como se puede acceder a los atributos de la clase?
p1.nombre = "Eduardo"

p2.nombre = "Ana" 
# Al editar un atributo de la instancia solamente se va a modificar en esa instancia y no en las otras
print(p1.nombre)
print(p2.nombre)

# si de momento al crear un statement (bloque de codigo) y este no tenemos lista la logica, se le pone "pass" para que no me de errores de identacion y dejar la logica para mas tarde

# Si una clase al momento de crear su instancia quiero inicializar los atributos, entonces debemos usar el constructor
class Gato:
    # cuando creamos una funcion dentro de una clase, esta pasa a llamarse metodo (porque solo va a funcionar dentro de la clase)
    # en python SIEMPREEE el primer parametro de un metodo es "self" (asi mismo), sirve para indicar que los cambios que hagamos se realicen a la misma instancia de la clase
    # en python no hay this, se usa self
    
    # Si creo un atributo pero este no lo pongo dentro del inicializador, este atributo no se configurara cuando cree la instancia pero igual se puede acceder a el 
    sexo = "Masculino"
    def __init__(self, nombrecito, raza, peso):
        # Para usar cualquier atributo o metodo de la misma clase usamos el "self"
        self.nombre = nombrecito
        self.raza = raza
        self.peso = peso
        # las variables que yo cree dentro de __init__ estos seran creados como atributos de la clase y podran ser usados en todos sus metodos

g1 = Gato("Michi", "Persa", 2.5)
print(g1.sexo)
# g1.sexo = "Afrodita"
print(g1.nombre)
# Para ti que significa el self, y que significa una clase