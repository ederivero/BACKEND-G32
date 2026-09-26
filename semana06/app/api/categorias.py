# Ahora todos los metodos (GET, POST, PUT, DELETE) se definiran como metodos de una clase
from flask_restful import Resource, request
from app.schemas import CategoriaSerializer
from pydantic import ValidationError
from app.models import Categoria
from app.extensions import db

class CategoriaController(Resource):
    def get(self):
        return {
            "message":"Las categorias son:"
        } # Su codigo de estado por defecto es 200

    def post(self):
        data = request.get_json()
        # Siempre hay que validar la data antes de mandarla a la bd
        # Si al momento de validar la informacion falla, emitira un error de tipo ValidationError
        try:
            informacionSerializada = CategoriaSerializer.model_validate(data)
            print(informacionSerializada)

            # Ahora que sabemos que la info es correcta, procedemos con el guardado en la bd
            # INSERT INTO categorias (nombre) VALUES (...);
            nuevaCategoria = Categoria(nombre = informacionSerializada.nombre)
            # Aca agregamos el nuevo registro a la bd
            db.session.add(nuevaCategoria)
            # Guardamos el registro de manera permanente
            db.session.commit()

            return {
                "message":"Categoria creada exitosamente"
            }, 201 # Created
        except ValidationError as error:
            return {
                "message":"Error al crear la categoria",
                "content":error.errors()
            }, 405 # Bad Request