# File on same folder with name "db.py"
import db
from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey

class Usuario(db.Base):
	__tablename__ = 'usuarios'
	id=Column(Integer, primary_key=True)
	descripcion=Column('descripcion', Text)
	activo = Column('activo', Boolean)
	edad=Column(Integer)

class Comentario(db.Base):
	__tablename__ = 'comentarios'
	id=Column(Integer, primary_key=True)
	mensaje=Column(String(20))
	id_u=Column(Integer, ForeignKey('usuarios.id'))
