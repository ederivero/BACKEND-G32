from app.extensions import db
from sqlalchemy import Column, types

class Categoria(db.Model):
    __tablename__='categorias'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, unique=True, nullable=False)