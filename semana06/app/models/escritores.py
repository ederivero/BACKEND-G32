from app.extensions import db
from sqlalchemy import Column, types
from enum import Enum

# Tenemos que crear un enumerador , es decir, limitar a posibles valores 
class EstadoEscritor(Enum):
    # Al heredar de la clase Enum los atributos que coloquemos en esta clase se comportaran como valores para poder ser utilizados
    VIVO = 'VIVO'
    MUERTO = 'MUERTO'

class Escritor(db.Model):
    __tablename__ = 'escritores'

    id = Column(type_=types.Integer, autoincrement=True, primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellidos = Column(type_=types.Text, nullable=False)
    nacionalidad = Column(type_=types.Text)
    # Para colocar un valor por defecto, es decir, si al momento de crear un registro este no se le pasa el valor entonces usara el valor definido en `default`
    estado = Column(type_=types.Enum(EstadoEscritor), nullable=False, default=EstadoEscritor.VIVO)