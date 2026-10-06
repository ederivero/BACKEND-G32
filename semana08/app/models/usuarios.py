from app.extensions import db
from sqlalchemy import Column, types
from uuid import uuid4

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = Column(type_=types.UUID(), primary_key=True, default=uuid4)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text)
    correo = Column(type_=types.Text, nullable=False, unique=True)
    password = Column(type_=types.Text, nullable=False)