from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
# nos brindara el proceso automatico de una determinada operacion
from rest_framework.generics import (CreateAPIView, # crear
                                    DestroyAPIView, # eliminar
                                    ListAPIView, # devolver todos
                                    ListCreateAPIView, # devolver todos y creacion
                                    RetrieveAPIView, # devolver solo uno
                                    RetrieveDestroyAPIView, # devolver solo uno y ademas poder eliminar
                                    RetrieveUpdateAPIView, # eliminar y ademas poder actualizar
                                    RetrieveUpdateDestroyAPIView, # devolver solo uno y ademas poder actualizarlo o eliminarlo
                                    UpdateAPIView) # actualizar
from .models import Categoria
from .serializers import CategoriaSerializer

class CategoriasView(APIView):
    # al usar una APIView esto es muy similar al Resource de flask-restful en el cual se puede colocar los metodos http como metodos de la clase

    def get(self, request):
        categorias = Categoria.objects.all()
        # Si se pasa un conjunto de instancias estamos en la obligacion de colocar many=True para que el serializador pueda iterar y transforma cada una de las instancias
        dataSerializada = CategoriaSerializer(instance=categorias, many=True)
        # en django no se puede retornar directamente un diccionario sino que tiene que crearse la instancia de la clase Response
        return Response(data = {
            "content": dataSerializada.data
        })

    def post(self, request:Request):
        print(request.data)
        serializador = CategoriaSerializer(data= request.data)
        # Si la data es valida, significa que toda la info enviada es correcta y agrega toda la info al atibuto validated_data, sin embargo si esta mal, se almacenara los errores en un atributo llamado errors
        if serializador.is_valid():
            print(serializador.validated_data)
            # El serializador al esta vinculado con un modelo internamente jala la forma de guardarlo en la bd con el metodo save
            serializador.save()

            return Response(data={
                "message":"Categoria creada exitosamente",
                "content": serializador.data
            }, status= status.HTTP_201_CREATED)

        else:
            return Response(data={
                "message":"Error al crear la categoria",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

# GET | PUT | DELETE
class DevolverActualizarEliminarCategoriaView(RetrieveUpdateDestroyAPIView):
    # SELECT * FROM categorias
    # Es la forma en la cual la vista se comunicara con la bd
    queryset = Categoria.objects.all()
    
    # Es la forma en la cual la vista se comunicara con la data enviada por el cliente y la data enviada hacia el cliente
    serializer_class = CategoriaSerializer
    
    # lookup_field sirve para indicar el parametro que se usara para identificar la PK (llave primaria)
    lookup_field = 'id'

