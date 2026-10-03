from flask_restful import Resource, request
from pydantic import ValidationError, TypeAdapter
from datetime import datetime
from app.models import Libro
from app.extensions import db
from app.schemas import LibroSchema

class LibrosController(Resource):
    def post(self):
        data = request.get_json()
        try:
            dataValidada = LibroSchema.model_validate(data)
            # Cuando una instancia de clase, una funcion, un metodo espera recibir un conjunto de parametros definidos por nombre
            #  Libro(nombre='...', isbn='...', eliminado='...', prologo = '...', fechaPublicacion = '...')
            # Pero si tenemos la informacion en un dict
            # {
            #   "nombre":"...",
            #   "libro":"...",
            #   ...
            #}
            # entonces en vez de pasar los parametros uno por uno se puede usar el dict para convertir las llaves en nombres de parametros y sus valores como valor del parametro usando el **

            nuevoLibro = Libro(**dataValidada.model_dump())
            db.session.add(nuevoLibro)
            db.session.commit()

            resultado = LibroSchema.model_validate(nuevoLibro).model_dump(mode='json')
            
            return {
                "message":'Libro creado exitosamente',
                'content': resultado
            }, 201

        except ValidationError as error:
            return {
                'message':'Error al crear el libro',
                'content':error.errors()
            }

    def get(self):
        libros = db.session.query(Libro).filter(Libro.eliminado==False).all()
        adaptador = TypeAdapter(list[LibroSchema])
        informacion = adaptador.validate_python(libros)

        return {
            'content': adaptador.dump_python(informacion, mode='json')
        }


class LibroController(Resource):
    def delete(self,id):
        # Soft delete (eliminacion suave) porque no se elimina el registro como tal en la bd, si no que solo cambia su estado (col eliminado)
        
        # Cuando modificamos las columnas que queremos obtener del ORM esto ya no retorna como una instancia de la clase, sino que retorna como una tupla con todos los valores solicitados
        # SELECT id FROM libros WHERE id = '...' AND eliminado = false;
        libroEncontrado = db.session.query(Libro).with_entities(Libro.id).filter(Libro.id == id, Libro.eliminado == False).first()

        if not libroEncontrado:
            return {
                'message':'Libro no existe'
            },404

        # Tambien se puede realizar la actualizacion mediante el metodo update
        db.session.query(Libro).filter(Libro.id == id).update({
            Libro.eliminado: True
        })

        # Guardamos la informacion de manera permanente en la bd
        db.session.commit()

        return {
            'message':'Libro eliminado exitosamente'
        }


    def get(self,id):
        libroEncontrado = db.session.query(Libro).filter(Libro.id==id).first()

        if not libroEncontrado:
            return {
                "message":'El libro no existe'
            },404

        # Gracias al relationship creado en LibroCategoria se crea el atributo virtual en la clase de Libro con el nombre colocado en el parametro backref y cuando ingreso a este parametro podre obtener todas sus libroCategorias pertenecientes a este libro y del mismo podre podre acceder a la categoria a la que pertenece gracias al relationship , en este caso seria categorias
        # print(libroEncontrado.libro_categorias)
        # print(libroEncontrado.libro_categorias[0].categoria.nombre)
        
        categorias = []

        for libroCategoria in libroEncontrado.libro_categorias:
            categorias.append({
                "id": libroCategoria.categoria.id,
                "nombre": libroCategoria.categoria.nombre
            })

        resultado = {
            "id": libroEncontrado.id,
            "nombre": libroEncontrado.nombre,
            # strftime convierte una fecha a un string usando el patron definido,
            # a diferencia del metodo strptime que convierte un string a una fecha usando el patro de lectura
            "fechaPublicacion": datetime.strftime(libroEncontrado.fechaPublicacion,"%Y-%m-%d %H:%M:%S"), # ISO 8601 
            "prologo": libroEncontrado.prologo,
            "isbn": libroEncontrado.isbn,
            "categorias":categorias
        }


        return {
            'content': resultado
        }