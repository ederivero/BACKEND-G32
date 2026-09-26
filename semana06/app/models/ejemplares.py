from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum

class EstadoEjemplar(Enum):
    DISPONIBLE = 'DISPONIBLE'
    PRESTADO = 'PRESTADO'
    NO_DISPONIBLE = 'NO_DISPONIBLE'

class Ejemplar(db.Model):
    __tablename__='ejemplares'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    codigoInventario = Column(type_=types.VARCHAR(100), nullable=False, name='codigo_inventario')
    estado = Column(type_=types.Enum(EstadoEjemplar), default=EstadoEjemplar.DISPONIBLE)
    libroId = Column(ForeignKey('libros.id'), type_=types.Integer, nullable=False, name='libro_id')
    # No influye en la creacion y mantenimiento de la tabla
    # relationship crea un atributo en las clases Ejemplar y Libro que serviran para poder acceder a su informacion anidada, es decir, desde el Ejemplar podemos acceder a que Libro pertenece y desde el Libro podremos acceder a todos sus ejemplares mediante, en este caso, el nombre definido en back_ref. Entonces si ponemos 
    # libro1 = Libro() obtenemos el registro de la bd
    # libro1.ejemplares > dara toda la lista de los ejemplares que pertenecen a ese libro en formato de Lista
    # [<Ejemplar1>, <Ejemplar2>,...] 
    # ejemplarcito = Obtengo mi registro de ejemplar de la bd
    # ejemplarcito.libro > devolvera el libro al cual pertenece este ejemplar 
    libro = relationship('Libro', backref='ejemplares')