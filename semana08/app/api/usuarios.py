from flask_restful import Resource, request
from app.extensions import db
from app.schemas import RegistroUsuarioSchema, LoginUsuarioSchema, UsuarioSchema
from pydantic import ValidationError
from app.models import Usuario
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta

class RegistroController(Resource):
    def post(self):
        try:
            dataValidada = RegistroUsuarioSchema.model_validate(request.get_json())
            print(dataValidada)
            # Buscar si hay algun usuario que ya exista con ese correo
            # SELECT id FROM usuarios WHERE correo = '...';
            usuarioExistente = db.session.query(Usuario).with_entities(Usuario.id).filter(Usuario.correo == dataValidada.correo).first()

            if usuarioExistente:
                return {
                    'message':'Usuario ya existe'
                },400

            # Proceso del hashing de la password
            # 1. Generamos el texto de ayuda (salt)
            salt = gensalt()
            
            # 2. Convertimos el password a bytes
            password = dataValidada.password.encode()

            # 3. Hacemos el hashing de la password
            password_hasheada_bytes = hashpw(password,salt)

            # 4. Convertimos el hashing del password en bytes a str
            password_hasheada = password_hasheada_bytes.decode()

            # TODO ESTE PROCESO SE PUEDE RESUMIR EN UN SOLO PASO
            # password_hasheada = hashpw(dataValidada.password.encode(),gensalt()).decode()

            print(password_hasheada)
            # Podemos usar la informacion de la validacion directamente
            nuevoUsuario = Usuario(
                # correo = dataValidada.correo, 
                # password = password_hasheada, 
                # nombre = dataValidada.nombre, 
                # apellido = dataValidada.apellido

                # Ahora convertido la informacion validada a diccionar procedemos a quitar la propiedad password
                **dataValidada.model_dump(exclude={"password"}),
                # Para luego agregarsela como parametro a la clase
                password=password_hasheada
                )

            db.session.add(nuevoUsuario)
            db.session.commit()
            
            return {
                'message':'Usuario registrado exitosamente'
            }, 201
        
        except ValidationError as error:
            print(error.errors())
            return {
                'message':'Error al crear el usuario',
                # el context brinda informacion adicional sobre el error que se esta dando, muchas veces aca se almacena la instancia de nuestro error entonces para no mostrarlo cuando se envia al cliente se quita con el metodo include_context en False
                'content': error.errors(include_context=False)
            },400


class LoginController(Resource):
    def post(self):
        try:
            dataValidada = LoginUsuarioSchema.model_validate(request.get_json())
            usuarioEncontrado = db.session.query(Usuario).filter(Usuario.correo == dataValidada.correo).first()

            if not usuarioEncontrado:
                return {
                    'message':'Usuario no existe'
                },404
            # Convertimos tanto la password como la password hasheada a bytes
            password = dataValidada.password.encode()
            hashedPassword = usuarioEncontrado.password.encode()
            
            # checkpw sirve para que usando el hashing almacenado en la bd me diga si es o no es la password sin la necesidad de saber el valor inicial
            esLaPassword = checkpw(password,hashedPassword)

            if esLaPassword:
                jwt = create_access_token(identity=usuarioEncontrado.id, # Es el identificador de la jwt, a quien le pertenece 
                                    fresh= False, # Si queremos que esta JWT sea usada como un refresh jwt 
                                    expires_delta= timedelta(hours=8,minutes=5)) # Indica la duracion que tendra de validez esta JWT
                return {
                    'content': jwt
                }
            else:
                return {
                    'message':'Credenciales incorrectas'
                },400

        except ValidationError as error:
            return {
                'message':'Error al hacer el login',
                'content':error.errors(include_context=False)
            }

class UsuarioController(Resource):
    @jwt_required() # sirve para indicar que el metodo que va a tratar de acceder tenga que enviar de manera OBLIGATORIA la JWT sino sera rechazado
    def get(self):
        id = get_jwt_identity() # devolvera el identificador de la jwt, es decir, el valor contenido en jti dentro del payload

        usuarioEncontrado = db.session.query(Usuario).filter(Usuario.id == id).first()

        resultado = UsuarioSchema.model_validate(usuarioEncontrado).model_dump(mode='json')
        return {
            'content': resultado
        }
