from app.extensions import db
from sqlalchemy import Column, types, ForeignKey
from sqlalchemy.orm import relationship

class Prestamo(db.Model):
    __tablename__ ='prestamos'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    fechaPrestamo = Column(type_=types.Date, nullable=False, name= 'fecha_prestamo') 
    fechaDevolucion = Column(type_=types.Date, name='fecha_devolucion')
    usuarioId = Column(ForeignKey('usuarios.id'), type_=types.Integer, nullable=False, name='usuario_id')
    ejemplarId = Column(ForeignKey('ejemplares.id'), type_=types.Integer, nullable=False, name='ejemplar_id')

    # p1 = Prestamo(...) # prestamos 002
    # p1.fechaPrestamo # 2026-09-01
    # p1.usuarioId > es devuelto como un numero > 10
    # Si quiera obtener la informacion del usuario que hizo el prestamo
    # Rudimentariamente tendria que buscar en la bd otra consulta para obtener ese usuario
    # Pero gracias a la relationship podemos obtener la informacion del usuario mediante su atributo `usuario`
    # p1.usuario > Instancia de la clase usuario con toda su informacion
    # p1.usuario.nombre > Eduardo 
    # p1.usuario.id > 10
    # p1.ejemplar.codigoInventario > HFK7763
    usuario = relationship('Usuario', backref='prestamos')
    ejemplar = relationship('Ejemplar', backref='prestamos')