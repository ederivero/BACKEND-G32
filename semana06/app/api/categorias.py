# Ahora todos los metodos (GET, POST, PUT, DELETE) se definiran como metodos de una clase
from flask_restful import Resource, request
from app.schemas import CategoriaSchema
from pydantic import ValidationError, TypeAdapter
from app.models import Categoria
from app.extensions import db

class CategoriasController(Resource):
    def get(self):
        # SELECT * FROM categorias;
        categorias = db.session.query(Categoria).all()
        print(categorias)
        # TypeAdaptar es una clase que me permite modificar el Deserializador para poder agregarle que puedo pasarle un conjunto de instancias, ya que solamente aceptara una
        adaptador_categorias = TypeAdapter(list[CategoriaSchema])
        # validate_python se usa para poder hacer la validacion de la informacion proveniente de las instancias del modelo y convertirlas a instancias del Deserializador
        resultado = adaptador_categorias.validate_python(categorias)
        print(resultado)
        return {
            "message":"Las categorias son:",
            # dump_python convertimos el conjunto de instancias del deserializador a un formato que pueda ser devuelto, es decir, en este caso usaremos un formato json
            "content": adaptador_categorias.dump_python(resultado, mode='json')
        } # Su codigo de estado por defecto es 200

    def post(self):
        data = request.get_json()
        # Siempre hay que validar la data antes de mandarla a la bd
        # Si al momento de validar la informacion falla, emitira un error de tipo ValidationError
        try:
            print(CategoriaSchema.model_json_schema())  
            informacionSerializada = CategoriaSchema.model_validate(data)

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


class CategoriaController(Resource):
    # Esta sera la encargada de la gestion de una sola categoria (segun su id)
    def validarCategoria(self,id):
        # el filter se usa en comparacion > filter(Categoria.id == 1)
        # el filter_by se usa en asignacion > filter_by(id=1)
        # SELECT * FROM categorias WHERE id = ... LIMIT 1;
        categoriaEncontrada = db.session.query(Categoria).filter(Categoria.id == id).first()
        return categoriaEncontrada
    

    def get(self, id):
        categoriaEncontrada = self.validarCategoria(id)
        if not categoriaEncontrada:
            return {
                'message':'Categoria no existe'
            }, 404
        
        respuesta = CategoriaSchema.model_validate(categoriaEncontrada).model_dump()

        # cuando se pida una categoria por su id, devolver la cantidad de libros que contiene esa categoria

        return {
            'content': respuesta
        }

    def put(self, id):
        categoriaEncontrada = self.validarCategoria(id)
        if not categoriaEncontrada:
            return {
                'message':'Categoria no existe'
            }, 404

        categoriaValidada = CategoriaSchema.model_validate(request.get_json())

        # En la instancia que tengo de mi categoriaEncontrada puedo modificar la informacion
        categoriaEncontrada.nombre = categoriaValidada.nombre

        db.session.commit()

        # Ahora obtenemos la informacion actualizada desde la categoriaEncontrada para devolverla al cliente
        resultado = CategoriaSchema.model_validate(categoriaEncontrada).model_dump()
        return {
            'message':'Categoria modificada exitosamente',
            'content': resultado
        }

    def delete(self, id):
        categoriaEncontrada = self.validarCategoria(id)
        if not categoriaEncontrada:
            return {
                'message':'Categoria no existe'
            }, 404

        # DELETE FROM categorias WHERE id = ...;
        db.session.query(Categoria).filter(Categoria.id == id).delete()

        db.session.commit()

        # En los deletes permanentes se suele no retornar nada y solo retornar un estado 204 (No Content)
        return None,204
        