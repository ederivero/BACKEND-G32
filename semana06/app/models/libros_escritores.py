from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

class LibroEscritor(db.Model):
    __tablename__='libros_escritores'

    libroId = Column(
        ForeignKey(column='libros.id'), 
        type_=types.Integer, 
        nullable=False, 
        primary_key=True, 
        name='libro_id')
    
    escritorId = Column(
        ForeignKey(column='escritores.id'), 
        type_=types.Integer, 
        nullable=False, 
        primary_key=True, 
        name='escritor_id')

    libros = relationship('Libro', backref='libro_escritor')
    escritores = relationship('Escritor', backref='libro_escritor')