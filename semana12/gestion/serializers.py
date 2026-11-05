from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField
from .models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['is_staff','is_superuser', 'is_active']

class LoginSerializar(Serializer):
    correo = EmailField(required=True)
    password = CharField(required=True)