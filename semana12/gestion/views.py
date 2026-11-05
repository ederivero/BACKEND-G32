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
from .serializers import UsuarioSerializer, LoginSerializar
from .models import Usuario

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
    serializador = LoginSerializar(data=request.data)

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
    
    return Response(data={
        "content":""
    })


