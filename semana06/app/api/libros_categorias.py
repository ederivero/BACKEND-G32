from flask_restful import Resource, request
from app.extensions import db
from app.models import LibroCategoria, Categoria
from app.schemas import LibrosCategoriasSchema
from pydantic import ValidationError

class LibrosCategoriasController(Resource):
    def post(self):
        try:
            # el request.get_json() obtiene la data enviada por el cliente a traves del body y la convierte a un diccionario
            # {categoriaIds: [1,1,2,3,4,5]}
            dataValidada = LibrosCategoriasSchema.model_validate(request.get_json()) 
            # {categoriaIds: [1,2,3,4,5]}
            
            # [(1,),(2,),(3,)] > [1,2,3]
            registros = db.session.query(LibroCategoria).with_entities(LibroCategoria.categoriaId).filter(LibroCategoria.libroId == dataValidada.libroId).all()

            registroIds = [fila[0] for fila in registros]

            categoriasAAgregar = []
            for categoriaId in dataValidada.categoriaIds:
                if categoriaId not in registroIds:
                    categoriasAAgregar.append(categoriaId)

            for categoria in categoriasAAgregar:
                categoriaEncontrada = db.session.query(Categoria).with_entities(Categoria.id).filter(Categoria.id == categoria).first()
                if not categoriaEncontrada:
                    return {
                        'message':f'La categoria {categoria} no existe',
                    },400
                
                nuevoLibroCategoria = LibroCategoria(categoriaId = categoria, libroId = dataValidada.libroId)
                db.session.add(nuevoLibroCategoria)

            db.session.commit()
            return {
                'message':'Categorias agregada a los libros exitosamente'
            },201
        
        except ValidationError as error:
            return {
                'message':'Error al crear las categorias del libro',
                'content': error.errors()
            }