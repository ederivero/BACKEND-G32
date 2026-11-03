from rest_framework.serializers import ModelSerializer
from .models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['is_staff','is_superuser', 'is_active']