from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import UsuarioSerializer


class UsuariosView(APIView):
    def post(self, request: Request):
        serializador = UsuarioSerializer(data=request.data)

        if serializador.is_valid():

            print(serializador.validated_data)
            return Response(data={
                "message":"Usuario registrado exitosamente"
            })

        else:
            return Response(data={
                "message":"Error al crear el usuario",
                "content":serializador.errors
            }, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        pass