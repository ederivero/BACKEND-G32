from flask_restful import Resource, request
from app.extensions import db
from app.schemas import RegistroUsuarioSchema
from pydantic import ValidationError

class RegistroController(Resource):
    def post(self):
        try:
            dataValidada = RegistroUsuarioSchema.model_validate(request.get_json())
            print(dataValidada)

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