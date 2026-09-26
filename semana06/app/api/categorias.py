# Ahora todos los metodos (GET, POST, PUT, DELETE) se definiran como metodos de una clase
from flask_restful import Resource

class CategoriaController(Resource):
    def get(self):
        return {
            "message":"Las categorias son:"
        } # Su codigo de estado por defecto es 200

    def post(self):
        return {
            "message":"Categoria creada exitosamente"
        }, 201 # Created