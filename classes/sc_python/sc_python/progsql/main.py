import db
from modelos import *

def Insertar():
	usr=Usuario(descripcion='jugador 2', activo=True, edad=20)
	db.session.add(usr)
	
	cm=Comentario(mensaje='Bueno juego', id_u=1)
	db.session.add(cm)

	db.session.commit()
	
	print(usr.id, usr.descripcion)
	print(cm.id, cm.mensaje)

if __name__ == "__main__":
	db.Base.metadata.create_all(db.motor)
	# Insertar()
	
	con1=db.session.query(Usuario).get(1)
	print(type(con1), con1.id, con1.descripcion)

	con2=db.session.query(Usuario).all()

	for u in con2:
		print(u.id, u.descripcion)
	
	con3=db.session.query(Usuario).count()
	print("cantidad de registros", con3)

	con4=db.session.query(Usuario).filter(Usuario.id==1)
	# print(con4)

	for u in con4:
		print(u.id, u.descripcion)




