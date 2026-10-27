from rest_framework.serializers import ModelSerializer
from .models import Categoria, Producto

# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class CategoriaSerializer(ModelSerializer):

    class Meta:
        model = Categoria
        # siempre debemos colocar una de los siguientes atributos
        # fields | exclude
        # sirve para indicar al serializador que campos (atributos) vamos a utilizar para hacer la validacion
        # fields = ["id", "nombre"]
        # Pero si se va a utilizar todos los campos del modelo
        # fields = "__all__"
        # Todos los campos menos el nombre
        exclude = ["eliminado"]

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        exclude = ["eliminado"]

class ProductoDetalleSerializer(ModelSerializer):
    class Meta:
        model = Producto
        exclude = ["eliminado"]
        # Podemos acceder a la informacion que esta adyacente a este modelo, es decir, si se pone 1 ingresaremos 1 nivel y si ponemos 2 ingresamos 2 niveles (si hay)
        depth = 1