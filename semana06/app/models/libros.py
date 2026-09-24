from app.extensions import db
from sqlalchemy import Column, types

class Libro(db.Model):
    __tablename__='libros'

    id = Column(autoincrement=True, primary_key=True, type_=types.Integer)
    nombre = Column(nullable=False, type_=types.Text)
    fechaPublicacion = Column(name='fecha_publicacion', type_=types.Date)
    prologo = Column(type_=types.Text)
    isbn = Column(type_=types.VARCHAR(20), unique=True, nullable=False)