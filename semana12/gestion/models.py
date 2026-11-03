from django.db import models
from uuid import uuid4
# AbstractUser te permite agregar nuevas columnas a la configuracion inicial del auth_user (name, last_name, password, email, is_superuser, is_staff, is_active, last_login)
# AbstractBaseUser te permite modificar por completo las columnas y propiedades el auth_user
# PermissionsMixin sirve para configurar como estara relacionada la nueva tabla de auth_user con relacion a los permisos (auth_groups, auth_user_permissions)
# BaseUserManager es el administrador sobre algunos comandos de la terminal como por ejemplo cuando se manda a a llamar al createsuperuser este manejara ese comportamiento
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class ManejadorUsuario(BaseUserManager):
    # Este sera el metodo que se llamara cuando en la terminal se quiera crear un superusuario (py manage.py createsuperuser)
    def create_superuser(self, nombre, correo,password):
        # Validamos si el correo no esta vacio
        if not correo or len(correo) == 0:
            raise ValueError("El correo es obligatorio")

        # normalize_email quita los espacios a los laterales y pone todo en minusculas y remueve caracteres especiales como tildes u otros 
        # EdUaRdO@gmail.com > eduardo@gmail.com
        correoNormalizado = self.normalize_email(correo)

        # con esto creamos la nueva instancia (registro) del usuario
        nuevoUsuario = self.model(correo = correoNormalizado, nombre = nombre)
        # set_password se encarga de generar el hash del password y guardarlo en la columna password
        nuevoUsuario.set_password(password)

        # Ahora modificamos los campos que usa el panel administrativo
        # is_superuser | is_staff
        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True

        # Guardamos el registro en la bd
        nuevoUsuario.save()

class Especialidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.TextField()

    class Meta:
        db_table = 'especialidades'    

# Vamos a usar el auth_user dentro de usuario
# Cambiamos la herencia de modelo comun y corriente al modelo encargado del auth_user
# Y tambien heredamos la forma en la cual se manejara los permisos del panel administrativo para el auth_user  
class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid4)
    nombre = models.TextField()
    apellidos = models.TextField(null=True)
    sexo = models.TextField()
    correo = models.TextField(unique=True)
    password = models.TextField()

    # Si aun queremos usar el panel administrativo nos vemos en la obligacion de agregar estos atributos
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Este atributo servira para indicar cual es el atributo que usare para poder identificar al usuario al momento de hacer login en el panel administrativo
    USERNAME_FIELD = 'correo'

    # Este atributo sirve para indicar que cuando se quiera crear un superusuario en la terminal que campos se deberia de solicitar 
    # No se debe de colocar el mismo atributo que el username_field porque ya esta implicito y asi mismo el password SIEMPRE sera solicitado
    REQUIRED_FIELDS = ['nombre']

    # Modificamos el comportamiento de nuestro auth_user y le asignamos la forma de creacion de un superusuario en la terminal
    objects = ManejadorUsuario()

    class Meta:
        db_table='usuarios'

class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    colegiatura = models.TextField()
    usuario = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, db_column='usuario_id')

    class Meta:
        db_table = 'doctores'    

class Paciente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    telefono = models.TextField(null=True)
    peso = models.FloatField(null=True)
    estatura = models.FloatField(null=True)
    usuario = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, db_column='usuario_id')

    class Meta:
        db_table = 'pacientes'

class EspecialidadDoctor(models.Model):
    # Cuando queremos crear una llave primaria compuesta en django tenemos la clase CompositePrimaryKey en la cual se debe colocar todas las columnas que involucraran a la creacion de esa llave primaria, esto solo se debe usar cuando se usa dos o mas columnas. esta clase SIEMPRE debe tener el atributo llamado pk (Primary Key)
    pk = models.CompositePrimaryKey("doctor_id","especialidad_id")
    doctor = models.ForeignKey(to=Doctor, on_delete=models.PROTECT, db_column='doctor_id')
    especialidad = models.ForeignKey(to=Especialidad, on_delete=models.PROTECT, db_column='especialidad_id')

    class Meta:
        db_table = 'especialidades_doctores'

ESTADO_CITAS = {
    # La llave sera usada en la bd mientras que su valor sera mostrado en el panel administrativo, aun asi no se use el panel administrativo siempre se debe colocar ambos valores
    "CONFIRMADO": "CONFIRMADO",
    "CANCELADO":"CANCELADO",
    "AGENDADO":"AGENDADO"
}

class Cita(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    fecha = models.DateField()
    horaInicio = models.TextField(db_column='hora_inicio')
    horaFin = models.TextField(db_column='hora_fin')
    estado = models.TextField(choices=ESTADO_CITAS, default=ESTADO_CITAS['AGENDADO'])
    observacion = models.TextField(null=True)
    consultorio = models.TextField(null=True)
    doctor = models.ForeignKey(to=Doctor, on_delete=models.PROTECT, db_column='doctor_id' )
    paciente = models.ForeignKey(to=Paciente, on_delete=models.PROTECT, db_column='paciente_id')

    class Meta:
        db_table='citas'