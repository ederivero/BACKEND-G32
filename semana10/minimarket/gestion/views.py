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
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view

from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer, ProductoDetalleSerializer, GenerarUrlAWSSerializer
from uuid import UUID
from boto3 import client
from os import getenv
from urllib.parse import unquote

class CategoriasView(APIView):
    # al usar una APIView esto es muy similar al Resource de flask-restful en el cual se puede colocar los metodos http como metodos de la clase

    def get(self, request):
        # SELECT * FROM categorias WHERE eliminado = FALSE
        categorias = Categoria.objects.filter(eliminado=False).all()
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
# Si mi vista generica deja de ser generica entonces la puedo convertir en un viewset en el cual
# post > create
# get > retrieve
# get > list (si se va a retornar varios registros)
# put > update
# delete > destroy
# patch > partial_update
class DevolverActualizarEliminarCategoriaView(RetrieveUpdateDestroyAPIView):
    # SELECT * FROM categorias
    # Es la forma en la cual la vista se comunicara con la bd
    queryset = Categoria.objects.all()
    
    # Es la forma en la cual la vista se comunicara con la data enviada por el cliente y la data enviada hacia el cliente
    serializer_class = CategoriaSerializer
    
    # lookup_field sirve para indicar el parametro que se usara para identificar la PK (llave primaria)
    lookup_field = 'id'

    # Devolver solo una categoria
    def retrieve(self, request, id):
        # al usar el retrieve | update | destroy siempre lo enviara como 2do parametro
        categoriaEncontrada = Categoria.objects.filter(eliminado=False, id = id).first()
        
        if not categoriaEncontrada:
            return Response(data={
                "message":"Categoria no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        dataSerializada = self.serializer_class(instance= categoriaEncontrada)

        return Response(data={
            "content": dataSerializada.data
        })

    def update(self, request, id):
        categoriaEncontrada = Categoria.objects.filter(eliminado=False, id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                "message":"Categoria no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = self.serializer_class(data=request.data)
        if serializador.is_valid():
            serializador.update(categoriaEncontrada,serializador.validated_data)

            return Response(data={
                "message":"Categoria actualizada exitosamente",
                "content": serializador.data
            })

        else:
            return Response(data={
                "message":"Error al actualizar la categoria",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id):
        categoriaEncontrada = Categoria.objects.filter(eliminado=False, id = id).first()
        if not categoriaEncontrada:
            return Response(data={
                "message":"Categoria no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        # Cambiamos el estado de eliminado a verdadero
        categoriaEncontrada.eliminado = True
        categoriaEncontrada.save()

        return Response(data=None, status=status.HTTP_204_NO_CONTENT)

class ProductosView(ViewSet):
    def create(self, request: Request):
        serializador = ProductoSerializer(data=request.data)
        # Aca validar si la categoria enviada no ha sido eliminada, si esta eliminada entonces no proceder con la creacion del producto
        categoriaEncontrada =Categoria.objects.filter(id= request.data.get("categoria"), eliminado=False).first()
        if not categoriaEncontrada:
            return Response({
                "message":"Error al crear el producto",
                "content": "Categoria no existe"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if serializador.is_valid():
            serializador.save()

            return Response(data={
                "message":"Producto creado exitosamente",
                "content": serializador.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "message":"Error al crear el producto",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request: Request):
        # Al usar el get en un query param solamente retornara la primera informacion del query param, es decir, si se envia una lista solamente tomara el primero , en cambio, el getlist obtiene todos los valores y los retornar en formato de lista para poder ser iterables
        categoria = request.query_params.getlist('categoria')
        nombre = request.query_params.get('nombre')

        filtros = {
            "eliminado": False
        }
        
        if categoria:
            # https://docs.djangoproject.com/en/6.1/ref/models/querysets/#field-lookups
            filtros["categoria__in"] = []

            for categoriaId in categoria:
                # Aca hacemos la validacion si el id de la categoria es UUID valido, para evitar algun error pero del lado de la base de datos
                try:
                    UUID(categoriaId)
                except:
                    return Response(data={
                        "message": f"El id de la categoria {categoriaId} es invalido"
                    })
                
                categoriaEncontrada = Categoria.objects.filter(id = categoriaId, eliminado = False).first()
                print(categoriaId, categoriaEncontrada)
                if categoriaEncontrada:
                    filtros["categoria__in"].append(str(categoriaEncontrada.id))

            # Validamos que si al final todas las categorias enviadas no existen entonces no agregamos ese filtro a la variable        
            if len(filtros["categoria__in"]) == 0:
                del filtros["categoria__in"]

        if nombre:
            # en SQL al usar el % en una busqueda de LIKE o ILIKE estamos indicando que no interesa que caracteres vienen antes o vienen despues
            # icontains > es en SQL un ILIKE, cuando se usa icontains ya no es necesario agregar % al comienzo ni al final 
            filtros["nombre__icontains"] = nombre

        # al usar el ** en un metodo y ese sea un diccionario estaremos indican que las llaves del diccionarion se convertiran a parametros y sus valores se convertir a los valores de los parametros , es decir data = {"nombre": "eduardo"} > **data > (nombre="eduardo")
        productos = Producto.objects.filter(**filtros).all()
        serializador = ProductoSerializer(instance= productos, many=True)
        return Response(data={
            "content":serializador.data
        })


class ProductoView(ViewSet):
    def retrieve(self, request:Request, id):
        productoEncontrado = Producto.objects.filter(id=id, eliminado=False).first()

        if not productoEncontrado:
            return Response(data={
                "message":"Producto no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        print(productoEncontrado.categoria.nombre)
        serializador =ProductoDetalleSerializer(instance = productoEncontrado)

        return Response(data={
            "content": serializador.data
        })

    def destroy(self, request:Request, id):
        productoEncontrado = Producto.objects.filter(id=id, eliminado=False).first()
        
        if not productoEncontrado:
            return Response(data={
                "message":"Producto no existe"
            }, status=status.HTTP_404_NOT_FOUND)

        # Realizamos el soft delete cambiando el estado del eliminado del producto a True y lo guardamos en la bd
        productoEncontrado.eliminado = True
        productoEncontrado.save()

        return Response(data=None, status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['POST'])
def crearUrlParaSubirArchivo(request:Request):
    # https://docs.aws.amazon.com/boto3/latest/guide/s3-presigned-urls.html
    # https://docs.aws.amazon.com/boto3/latest/reference/services/s3/client/generate_presigned_url.html
    serializador = GenerarUrlAWSSerializer(data=request.data)
    if serializador.is_valid():
        fileName = serializador.validated_data.get("fileName")
        ext = serializador.validated_data.get("ext")
        contentType = serializador.validated_data.get("contentType")
        folder = serializador.validated_data.get("folder", "/")
        
        s3 = client('s3')

        url = s3.generate_presigned_url(
            ClientMethod = 'put_object',
            Params={
                "Bucket":getenv('BUCKET_NAME'),
                "Key": folder + fileName + ext,
                "ContentType":contentType
            },
            ExpiresIn=150
        )
        return Response(data={
            "content": unquote(url)
        })
    else:
        return Response(data={
            "message":"Error al generar la URL",
            "content": serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)
