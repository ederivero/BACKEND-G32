from rest_framework.serializers import ModelSerializer
from .models import Categoria

# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class CategoriaSerializer(ModelSerializer):

    class Meta:
        model = Categoria
        # siempre debemos colocar una de los siguientes atributos
        # fields | exclude
        # sirve para indicar al serializador que campos (atributos) vamos a utilizar para hacer la validacion
        # fields = ["id", "nombre"]
        # Pero si se va a utilizar todos los campos del modelo
        fields = "__all__"
        # Todos los campos menos el nombre
        # exclude = ["nombre"]