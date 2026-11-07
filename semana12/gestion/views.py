from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
                                        IsAuthenticated, # Obligara a que si no hay una token y esta sea valida no permitira ingresar al endpoint
                                        IsAdminUser, # Validara que el usuario que quiera consultar sea is_superuser y sino no podra continuar
                                        IsAuthenticatedOrReadOnly, # Validara que si el metodo es GET normal podra continuar pero si no es GET la JWT sera obligatoria y tiene que ser valida
                                        AllowAny # Permitira que cualquiera pueda consultar cualquier metodo sin la necesidad de enviar una JWT, esto es el valor predeterminado
                                        )

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .serializers import UsuarioSerializer, LoginSerializer, DoctorSerializer, PacienteSerializer, EspecialidadSerializer
from .models import Usuario, Paciente, Doctor, Especialidad
from .pagination import PaginacionEstandar
from django.db import connection, reset_queries


@api_view(http_method_names=['POST'])
def registroUsuario(request: Request):
    serializador = UsuarioSerializer(data=request.data)

    if serializador.is_valid():

        print(serializador.validated_data)
        nombre = serializador.validated_data.get('nombre')
        correo = serializador.validated_data.get('correo')
        sexo = serializador.validated_data.get('sexo')
        password = serializador.validated_data.get('password')
        nuevoUsuario = Usuario(nombre=nombre,correo=correo,sexo=sexo)

        # EL modelo auth_user tiene un metodo set_password que genera el hash de la contraseña y lo guarda en el campo de password
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()

        return Response(data={
            "message":"Usuario registrado exitosamente"
        },status=status.HTTP_201_CREATED)

    else:
        return Response(data={
            "message":"Error al crear el usuario",
            "content":serializador.errors
        }, status = status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['POST'])
def loginManual(request:Request):
    serializador = LoginSerializer(data=request.data)

    if serializador.is_valid():
        correo = serializador.validated_data.get('correo')
        password = serializador.validated_data.get('password')
        usuarioEncontrado = Usuario.objects.filter(correo = correo).first()
        # Aca se deberian agregar mas filtros como si esta habilitado, si tiene los permisos necesarios, etc.
        if not usuarioEncontrado:
            return Response(data={
                "message":"El usuario no existe"
            }, status=status.HTTP_400_BAD_REQUEST)

        # Este metodo es un metodo propio del auth_user que al heredar en la clase de usuario podemos utilizarlo
        esLaPassword = usuarioEncontrado.check_password(password)
        if esLaPassword:
            # Para generar tokens necesito llamar a la clase RefreshToken y esta me retornara token de acceso y de refresco para la sesion
            token = RefreshToken.for_user(usuarioEncontrado)
            token2 = AccessToken.for_user(usuarioEncontrado)
            return Response(data={
                "content": {
                    "accessToken": str(token.access_token),
                },
                "token": str(token2)
            })
        else:
            return Response(data={
                "message":"Credenciales invalidas"
            }, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(data={
            "message":"error al hacer el login",
            "content":serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)

# DRF tiene un formato de poder requerir o no la autenticacion en los metodos que sea necesario mediante el decorador permission_clases o dentro de las vistas usando el atributo permissions_classes
@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def perfilUsuario(request: Request):
    print(request.auth) # retorna la JWT directa
    print(request.user) # retorna la instacia que le pertenece al usuario

    usuarioActual = request.user
    serializador = UsuarioSerializer(instance= usuarioActual)
    return Response(data={
        "content":serializador.data
    })


@api_view(http_method_names=['POST'])
@permission_classes([IsAuthenticated])
def configurarDoctor(request:Request):
    # la info del usuario viene en request.user
    # 1. validar si el usuario existe
    usuarioExiste = Usuario.objects.filter(id = request.user.id).first()
    if not usuarioExiste:
        return Response(data={
            "message":"El usuario no existe"
        }, status=status.HTTP_404_NOT_FOUND)
    # 2. un usuario no puede ser doctor y paciente entonces validar que este usuario no sea paciente, si lo es no se debe continuar
    pacienteUsuario = Paciente.objects.filter(usuario = usuarioExiste.id).first()
    if pacienteUsuario :
        return Response(data={
            "message":"El usuario ya es un paciente"
        }, status=status.HTTP_400_BAD_REQUEST)
    # 3. guardar la informacion del doctor
    #  
    # Agregamos el id del usuario proveniente del JWT a el id del usuario que usara el doctor en el registro
    request.data['usuario']= usuarioExiste.id
    serializador = DoctorSerializer(data = request.data)
    if serializador.is_valid():
        serializador.save()
        return Response(data={
            "message":"Doctor creado exitosamente",
            "content": serializador.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(data={
            "message":"Error al crear el registro",
            "content":serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=['POST'])
@permission_classes([IsAuthenticated])
def configurarPaciente(request:Request):
    # 1. validar si el usuario existe
    usuarioExiste = Usuario.objects.filter(id = request.user.id).first()
    if not usuarioExiste:
        return Response(data={
            "message":"El usuario no existe"
        }, status=status.HTTP_404_NOT_FOUND)
    # 2. un usuario no puede ser doctor y paciente entonces validar que este usuario no sea paciente, si lo es no se debe continuar
    doctorUsuario = Doctor.objects.filter(usuario = usuarioExiste.id).first()
    if doctorUsuario :
        return Response(data={
            "message":"El usuario ya es un doctor"
        }, status=status.HTTP_400_BAD_REQUEST)
    # 3. guardar la informacion del paciente
    #  
    # Agregamos el id del usuario proveniente del JWT a el id del usuario que usara el doctor en el registro
    request.data['usuario']= usuarioExiste.id
    serializador = PacienteSerializer(data = request.data)
    if serializador.is_valid():
        serializador.save()
        return Response(data={
            "message":"Paciente creado exitosamente",
            "content": serializador.data
        }, status=status.HTTP_201_CREATED)
    else:
        return Response(data={
            "message":"Error al crear el registro",
            "content":serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class EspecialidadesView(APIView):
    def get(self, request: Request):
        # Reinicia toda la cola de consultas que se ha realizado para evitar que en el for se puedan mostrar consultas pasadas y confunda la data
        reset_queries()

        nombre = request.query_params.get('nombre')
        print(nombre)
        # Django no obtiene de manera automatica los registros, porque el queryset es PEREZOSO, Django solamente obtiene la informacion de la base de datos hasta usar los datos
        especialidades = Especialidad.objects.all()

        if nombre:
            # ILIKE 
            # al momento de agregar un filtro adicional a una query previamente definida tenemos que sobreescribir la intancia previa para que surga efecto, porque si solamente le agregamos el filtro entonces no se agregara a la instancia previa
            especialidades = especialidades.filter(nombre__icontains = nombre.strip())

        paginador = PaginacionEstandar()
        # le pasamos la informacion que va a utilizar para poder obtener los registros de la bd, asi mismo le pasamos el request en cual contendra los query_params para poder hacer la paginacion y le pasamos la vista en el caso que estemos usando templates para que esta pueda ser renderizada sin problema, en nuestro caso no es necesario esa informacion
        resultado = paginador.paginate_queryset(especialidades,request, view=self)
        serializador = EspecialidadSerializer(instance = resultado, many=True)

        print(resultado)
        # convertira la informacion proveida de la consulta a la bd y la serializara de manera correcta antes de poder retornarla al cliente
        respuesta = paginador.get_paginated_response(serializador.data)

        # For para debug en el cual solo se usa cuando queremos validar cuantas y que consultas se estan realizando en la bd en determinado endpoint
        for consulta in connection.queries:
            # Imprime todas las consultas que sealizan en la bd
            print(consulta["sql"])
        return respuesta

    def post(self, request:Request):
        # Implementar el post
        # para crear una nueva especialidad
        serializador = EspecialidadSerializer(data = request.data)

        if serializador.is_valid():
            serializador.save()
            return Response(data={
                "message":"Especialidad creada exitosamente",
                "content": serializador.data
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                "message":"Error al crear la especialidad",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)