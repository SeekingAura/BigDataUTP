# Scripts en mongo

## Ejecución directa cmd
Mongo su kernel está en javascript, entonces los scripts han de ser archivos *.js* para ejecutar fe forma sencilla desde command line es con lo siguiente

```bash
mongo < archivo.js
```

Donde el "archivo.js" es el que contiene el script

Un ejemplo

```bash
nano ejemplo1.js
```

Colocar

```javascript
use vehiculos;
show collections;
db.automotor.findOne({'MARCA':'MAZDA'});
```

Y luego 
```bash
mongo < ejemplo1.js
```

## Ejecución cmd con string directo
el comando **mongo** tiene un parametro el cual es eval, este permite ejecutar a razón de una cadena de caracteres las instrucciones que contenga ese string, es util cuando hay transitividad de datos o ejecuciones sencillas de manera externa. 

Un ejemplo, mostrar un resultado del collection automotor la llave marca MAZDA, luego está indicada la base de datos sobre la cual se ejecuta la instrucción (para este caso la DB vehiculos)

```bash
mongo --eval "db.automotor.findOne({'MARCA':'MAZDA'});" vehiculos
```

# parametrizar
El hecho de parametrizar es el hacer scripts del la base de datos (en este caso los js) y hacer el script del lenguaje de programación para ejecutar esos scripts.

Es como decir un control "ordenado" del sistema de archivos mediante algun tipo de "programa" en este caso serán archivos


# pymongo
Es una libreria que permite el uso de comandos de mongo mediante instrucciones mas al estilo python haciendo qeu sea mas facil la transitividad de datos o modificación de los mismos.

```python
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
reg=db.automotor.find_one()

print(reg)
````

En este tambien se permiten los filtros y demas capacidades que tiene como tal mongo

```python
from pymongo import *


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
```

