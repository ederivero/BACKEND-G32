from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField
from .models import Usuario, Doctor, Paciente

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['is_staff','is_superuser', 'is_active', 'user_permissions', 'last_login', 'groups']

        # Si queremos condicionar un atributo a que sea solo lectura o solo escritura entonces se recomienda usar los extra_kwargs
        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }

class LoginSerializer(Serializer):
    correo = EmailField(required=True)
    password = CharField(required=True)

class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'