from pymongo import *

'''
Establecer la conexion requiere 
# ip del servidor
# requiere puerto
'''


ip = 'localhost'
port=27017
db_name='vehiculos'
client=MongoClient(ip, port)

db=client[db_name]

# Equivalent to findOne on mongo
respuesta=db.automotor.find({'MARCA':'MAZDA'})

for v in respuesta:
	print(v['PLACA'], v['MODELO'])


