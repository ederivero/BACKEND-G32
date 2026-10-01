from flask_restful import Resource, request
from app.extensions import db
from app.models import LibroCategoria

class LibrosCategoriasController(Resource):
    def post(self):
        pass
