from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey

# Connect to db
motor=create_engine('mysql+pymysql://admin:Bigdata-2020@localhost:3306/sqlejemplo')

# Definition about sesion
Session = sessionmaker(bind=motor)

# Login to database
sesion = Session()

# Definition about library base
Base=declarative_base()

class Usuario(Base):
	__tablename__= 'usuarios'
	id=Column(Integer, primary_key=True)
	descripcion=Column('descripcion', Text)
	activo=Column(Boolean)
	edad=Column(Integer)

class Comentario(Base):
	__tablename__ = 'comentarios'
	id=Column(Integer, primary_key=True)
	mensaje=Column(String(20))
	id_u=Column(Integer, ForeignKey('usuarios.id'))


Base.metadata.create_all(motor)
