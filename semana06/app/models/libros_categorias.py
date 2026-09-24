from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

class LibroCategoria(db.Model):
    __tablename__='libros_categorias'

    libroId = Column(
        ForeignKey(column='libros.id'), 
        nullable=False, 
        name='libro_id', 
        primary_key=True, 
        type_=types.Integer)
    
    categoriaId = Column(
        ForeignKey(column='categorias.id'), 
        nullable=False, 
        name='categoria_id', 
        primary_key=True, 
        type_=types.Integer)

    # Relationships
    # es la relacion pero a nivel del ORM, es decir, esto no afecta en la bd pero me sirve para poder acceder a los datos desde una entidad (libros) hacia sus libros_categoria
    # El relationship creara un atributo en tiempo de ejecucion para poder acceder desde la instancia de libro hacia todos sus libro_categorias
    libros = relationship('Libro', backref='libro_categoria')
    categorias = relationship('Categoria', backref='libro_categoria')