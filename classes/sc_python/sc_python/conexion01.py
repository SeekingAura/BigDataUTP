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

print(db)

# Equivalent to findOne on mongo
reg=db.automotor.find_one({'MODELO':2010, 'MARCA':'HYUNDAI'},{'_id':0, 'PLACA':1, 'MARCA':1, 'MODELO':1})

print(reg)

