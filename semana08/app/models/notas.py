from app.extensions import db
from sqlalchemy import types, Column, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

class Nota(db.Model):
    __tablename__='notas'

    id = Column(type_=types.UUID(), default=uuid4, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    eliminado = Column(type_=types.Boolean, default=True)
    descripcion = Column(type_=types.Text)
    usuarioId = Column(ForeignKey('usuarios.id'), nullable=False, name='usuario_id', type_=types.UUID())

    usuario = relationship('Usuario', backref='notas')