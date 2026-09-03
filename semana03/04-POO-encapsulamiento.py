class CuentaBancaria:
    def __init__(self, titular, saldo, cuenta):
        self.titular = titular
        self.saldo = saldo
        # Cuando se crea un atributo con un subguion este es protegido, es decir no se debe acceder fuera de la clase
        # Python es muy permisivo con los atributos protegidos, es decir, si me va a permitir acceder al atributo afuera de la clase pero es por una CONVENCION (buenas practicas) que no debo acceder a el fuera de la clase. Cosa que si se cumple en otros lenguajes de programacion como Java, C++, C#, entre otros
        # Si se pueden heredar hacia otras clases hijas
        self._cuenta = cuenta
        # Cuando el atributo empieza con doble subguion este es PRIVADO, ESTE NO SE PODRA ACCEDER
        # No se puede heredar hacia otras clases hijas
        self.__entidad_financiera = "BCP"


cuenta1 = CuentaBancaria("Eduardo", 500,"100-1323443434-201")
print(cuenta1.saldo)
# Se puede modificar los atributos que son PUBLICOS
cuenta1.saldo = 2500
print(cuenta1.saldo)
print(cuenta1._cuenta)
# print(cuenta1.__entidad_financiera) # AttributeError > error cuando el atributo no existe


# Para exponer atributos privados/protegidos de forma controlada se suele utilizar el decorador @property en vez de getters y setter como en Java
# getter | setter > son metodos que sirven para devolver (getter) y modificar (setter) el valor del atributo protegido o privado

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__apellido = "Xi"

    # Luego del decorador siempre se llama a un metodo porque el decorador modifica la funcion adyacente con la propiedad del decorador, en este caso, el decorador property sirve para definir la devolucion del contenido del atributo privado
    # Con el decorador property convertimos un metodo a un atributo y sirve mayormente para exponer el contenido de atributos privados y protegidos desde fuera de la clase
    @property
    def nombre(self):
        return self.__nombre

    # Asi mismo se puede utilizar los metodos para modificar y eliminar el contenido del atributo privado
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def apellido(self):
        return self.__apellido



p1 = Persona("Eduardo")
print(p1.nombre)
p1.nombre = "Renato"
print(p1.nombre)
print(p1.apellido)



# Crear una clase Usuario en el cual tengamos el nombre, correo, password. El password debe ser un atributo privado y solamente en el constructor inicializar el nombre y correo. Cuando se quiera modificar el password usar el @property y no permitir el ingreso de un string que tenga espacios o sea menor que 8 caracteres, y asi mismo cuando se quiera obtener el password devolver *******