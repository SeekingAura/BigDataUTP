# Mongo

## instalation de versión especifica

```
$ sudo apt-get install gnupg -y
```

```
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key del -
```

```
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
```

```
$ sudo apt-get update
```

```
$ sudo apt-get install -y mongodb-org
```


## Instalación de versión actual

```
$ sudo apt install mongodb
```

## Gestión

### Arranque del servicio
Iniciar el servicio manual
```
$ sudo service mongodb start
```

Iniciar el servicio automatico
```
$ systemctl start mongodb
```

Establecer el servicio de arranque al sistema
```
$ sudo systemctl enable mongodb
```

### Detener el servicio

```
sudo service mongodb stop

sudo systemctl stop mongod
```
### Reiniciar el servicio

```
sudo service mongodb restart

systemctl restart mongod
```
### Shell de mongo

```
mongo
```

## Gestionar base de datos

### Crear o seleccionar DB


```
use DATABASE_NAME
```

No hay un comando explicito para crear la base de datos o para accederla por lo cual este comando use es tanto para crear como para acceder.

Si la base de datos que se hace use no existe automaticamente se creará, en caso de que exista lo accederá (ADOC). Las no existentes existiran en el momento que se agrege algun dato.

### Ver base de datos actualmente seleccionada
```
db
```

### Ver bases de datos existentes
```
show dbs
```

lista todas las bases de datos existentes. Mongo ya cuenta con unas dbs por default uq gestionan el sistema de la DB, las cuales osn *admin*, *config*, *local*
## Gestionar datos de una DB
Los datos de mongo se almacenan en colecciones de datos, técnicmaente es el equivlaente a las Tablas en SQL. Estos comandos se realizan sobre la base de datos que se haya seleccionado antes.

Una colección viene a ser técnicamente los diccionarios que contienen la DB

### Crear colección
```
db.createCollection(name, options)
```

### Ver colecciones
```
show collections
```

### Borrar colección
```
db.COLLECTION_NAME.drop()
```

### Insertar datos a la colección
```
document={titulo:"Codigo Da Vinci",
autor: "Dan Brown",
temas: ["novela, "historia", "ficcion"]}
db.COLLECTION_NAME.insert(document)
```

### Buscar datos en las colecciones
```
db.COLECCION.find()
db.COLECCION.find().pretty()
```

#### Ejemplos de busqueda
Buscar documentos que contengan como titulo "Desaparecido" o "algo"
```
db.documentos.find({titulo: {$in : ["Desaparecido", "algo"]}}).pretty()
```

```
db.documentos.find({titulo: {$eq : "Desaparecido"}}).pretty()
```

Buscar cualquier datos que coincidan con los valores que se indicna en forma de "diccionario"

```
db.publicos.find({"cilindraje":120})
```
Limitar los resultados

```
db.COLECCION.find().limit(2)
```

Ver el primer dato
```
db.COLECCION.findOne()
```

## "updates" en la DB


### Update de reemplazar
```
db.libros.update({autor:"alguien"}, {autor:"otro", "titulo":"un titulo"})
```

Los "update" de la forma anterior son técnicamente "reemplazos" en los datos que tienen los colecction, aqui ene ste caso es a lo que coincida (diccionario de la izquierda) será reemplazado con el dato que hay en la derecha. Esto solo aplica con la PRIMERa ocurrencia que coincida con los datos de referencia

### Update agregar datos o modificar datos
El dato en el colection con llave **placa** que tenga valor "ABC100" agregar o editarle el valor de llave **marca** Dejando INTACTO los demas valores que tenga el dato
```
db.publicos.update({placa:'ABC100'},{$set:{marca:'HONDA'}})
```
Esto solo se relaizará sobre la PRIMERA ocurrencia. En caso de requerir una operación que se aplique sobre todos los datos coincidentes se debe usar otra instrucción

update_many -> El mismo update pero opera sobre TODOS los que coincidan en la instrucción

https://docs.mongodb.com/manual/reference/operator/query-comparison/


## Delete información en mongo
Borrar datos de una colección la clave está en las coincidencias

```
db.publicos.remove({marca:'HONDA'})
```

Esa instrucción borrará TODOS los datos que coincidan con lo indicado.

## Dump o copia de collections de mongodb

Esto seria un equivlaente a un dump en mysql de un collection hacer un "backup"
```
db.getCollection('publicos')
    .aggregate([
        { $out: 'publicos2' }
    ]);
```

En las "viejas" versiones de mongo se puede usar lo siguiente

```
db.collection.copyTo(newCollection)
```



## Tipos de datos de mongo
Los tipos de datos de mongo son los mismos que tiene una base de datos normal, sin embargo, su forma de tipo de dato es por cada dato qeu se acopla o adapta a razón del formato que este escrito el dato al momento de ser insertado


## Importar datos a mongo
Mongo puede traer datos que tengan alguna estructura conocida para que lo carge de forma "automatica" a una db y colección especifica.

En caso que no existe será creada, si no será agregado

```
mongoimport --db nombre_db --collection nombre_collection --type=csv --file nombre_archivo --headerline

mongoimport --db vehiculos --collection automotor --type=csv --file 
```

--db -> indica el nombre de db al cual será guardado la importación  
--collection -> indica el nombre de la colleccion en donde será guardado la importación  
--type -> indica el formato del archivo del cual se basa para la importación
--file -> indicar cual es el archivo para importar
--headerline -> indica que la primera linea es el header donde tiene el nombre de las llaves

# Model ETL - despues de 2012



