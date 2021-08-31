# ETL (Extraction, Transsaction, Load)

## Warehousing (almacenamiento)
* Sistema utilizado para almacenamiento de datos
* Posee funciones de generación de reportes
* Sistemas con frecuencia

## Data Warehousing Definition
El almacen de datos (Data warehouse) Se define como un sistema de recopilación de datos orintada a un objeto de observación, integrada, variable en el tiempo y no volátil enfocada en el proceso de toma de decisiones

**Orientada al objeto:** usada para analizar un área de estudio en particular. El objetivo como tal no es solo almacenar los datos, si no que el almacenamiento de los datos tiene un objetivo a razón de su almacenamiento.

**Integrada:** muestra datos procedentes de diferentes fuentes de datos  
**Variable en el tiempo:** Almacena datos historicos.  
**No volátil:** los datos almacenados en el almacen de datos no deben ser alterados.

# Tipos y/o procesos de warehousing

## Warehousing OLTP (On Line Transaction Processing System)
Refiere al **almacenamiento de datos mediante transacciones en linea**. Hace referencia al sistema de almacenamiento de datos de la empresa o **sistemas de datos** que fue actualizado (current data) que procede de diversas fuentes.

Usualmente utilizado por más de una aplicación, cada una de estas debe verificar permanentemente la consistencia de los datos. El como se almacena los datos para el sistema en SQL es impotante cada insersión ya que SQL es escritcto en sus campos. En el caso de No-SQL como Mongo no es tan estricto entonces no presenta mayor problema en las transacciones diversas. Suelen ser datos que requeire la aplicación para su funcionamiento

## Warehousing OLAP (On Line Analytical Processing System)
Hace referencia al sistema cuyo objetivo es analizar los datos para la **toma de decisiones** y la **planificación** en el modelo de negocios.

Tambien cumple funciones de ensamblaje de los diferentes modelos de datos.

En comparación con el OLTP la cantidad de datos que maneja es mucho menor. 

Los datos deben tener un proposito determinado para que de esta manera sea almacenado de tal forma que permita un "buen" proceso de analisis

# Softwares relacionados al warehouse
CRM (Customer Relationship Management)-> Seguimiento a los clientes  
ETL (Enterpresie Resource Planning) -> seguimiento a la planeación de la organización  
SCM (Supply Chain Management) -> Administración de la cadena de suplementos  

Estos software anteriores generan y/o entregan datos al Data Warehouse y de estos datos se pueden hacer analisis OLAP, mineria de datos, reportes entre otras actividades de analisis de datos.


# Base de datos Vs Almacen de datos

**Base de datos:** Típicmaente es un modelo OLTP para almacenamiento de aplicaciones  
**Almacén de datos:** acumulación de datos relacionados con una aplicación, *puede* incluir datos transacciones, archivos planos relacionados, datos heredados de otros sistemas, etc.


# Almacen de datos Vs Business Intelligent
**Business Intelligent** conjunto de técnicas y herramientas para la transformación de datos crudos en información significativa y útil para fines de análisis comercial.

**Almacén de datos** es una forma de almacenar datos y crear inforamción especifica sobre data seleccionados (Data mart). Los Data marts es un conjunto de datos asociados bajo un criterior o categorías sobre el que se busca generar algún tipo de explotación.

La BI aprovecha el almacen de datos para tomar decisiones o crear recomendaciones.

La información y los modelos basados en reglas (motores de inferencia) de datos se emplean para ayudar en la toma de decisiones junto con herramientas de análisis estadístico y minería de datos.

El almacén de datos no requeire del BI para realizar su trabajo. Las herramientas de generación de informes requeiren almacenes de datos para realizar su labor.


# Data mart
De un conjunto de datos ETL al dato entrante se le da diferentes etiquetas donde se clasifica la estructura del dato y se genran bases de datos "tematicas". Esas etiquetas hace que eso sea un Data mart.

# ETL
Se refiere al proceso de extracción, transformación y carga (Extraction, Transformation and Loading)

**Extraction:** se define como la extracción de datos de las fuentes las cuales pueden provenir de sistemas externos, base de datos o archivos planos.

**Transformación:** Procesos uqe transforman los datos como limpieza, integración o cualquier cosa que modifique los datos, hace referencia a cualquier proceso que genere cambio sobre el conjunto de datos.

**Carga:** Es la traslación de los datos transformados hacia los sistemas, base de datos o archivo plano destino donde se almacene el dato tratado


```javascript
db.getCollection('source')
    .aggregate([
        { $out: 'destination' }
    ]);
```

La gracia de usar una base de datos no sql permite que se adapte muy facilmente las diferentes estructuras de datos

# MongoDB more Querys
Los datos que hay en mongo como las DB o collections pueden exportarse para que asi permitan un analisis posterior o llevarlo a otros sistemas por ejemplo a un archivo CSV.

```bash
mognoexport --db=vehiculos --collection=sumatoria --type=csv --separator=, fields=_id,value --out=conteo_vehiculos.csv
```

## Aggregation, ensamblaje
Esta instrucción permite realizar una acción o ejecución que utiliza la salida de un dato como entrada de otra función o bien una cadena de entradas . En otras palabras una consulta que usa el resultado de otra consulta. Estas multiples consultas es dadas en una lista donde se ejecuta de izquierda a derecha




### Group o en SQL group By
De la collection *automotor* agrupar por la llave **MARCA** y esa Marca ponerla como campo **_id** en el resultado

```javascript
db.automotor.aggregate([{$group: {_id:'$MARCA'}}])
```


De la collection *automotor* agrupor por la llave **MARCA** guardar en un campo llamado **_id** y por cada elemento que sea del mismo sumarle 1 guardandolo en un campo llamado **cantidad**

```javascript
db.automotor.aggregate([{$group: {_id:'$MARCA', cantidad:{$sum:1}}}])
```

### Matching o '=' en mysql

Mostrar todos los vehiculos que sean de marca BMW
```
db.automotor.aggregate([{$match: {MARCA:'BMW'}}])
```

Obtener los vehiculos que son de 4 pasajeros (muy posiblemente taxis)
```javascript
db.automotor.aggregate([{$match: {PASAJEROS: 4}}])
```

### Exportar resultados a un collection

Obtener los behiculos de 4 pasajeros y guardar el resultado de esa consulta en una collection llamada **taxis**
```javascript
db.automotor.aggregate([{$match: {PASAJEROS: 4}}, {$out:'taxis'}])
```

### Count
Obtener la cantidad de datos o bien "filas" del collection taxis
```javascript
db.taxis.find().count()
```

sin embargo, solo funciona en collections, para hacerlo datos toca dar uso de sum. En este caso obtener vehiculos de 4 pasajeros y de marca MAZDA luego es agrupado por marca pero como es una unica marca que fue mazda se obtendrá el total de esos resultados
```javascript
db.automotor.aggregate([{$match: {PASAJEROS: 4, MARCA: 'MAZDA'}}, {$group:{_id:'$MARCA', can:{$sum:1}}}])
```

### project y alias o seleccionar campos a obtener y as 
Sirve para definir lo que se quiere tener en la salida. En otras plaabras es establecer de los resultados que se obtienen establecer que campos serán lso que se obtendrán de cada query. En el siguiente ejemplo al resultado de la query con match mostrar unicamente placa como placa y estado como estado

```javascript
db.automotor.aggregate([{$match: {PASAJEROS: 4, MARCA: 'MAZDA'}}, {$project:{placa:'$PLACA', estado:'$ESTADO'}}])
```

Por defecto se muestra el **_id** tambien, para omitirlo se debe agregar _id:0 al project

```javascript
db.automotor.aggregate([{$match: {PASAJEROS: 4, MARCA: 'MAZDA'}}, {$project:{_id:0, placa:'$PLACA', estado:'$ESTADO'}}])
```


### Sorting
en ocasiones cuando hay muchos datos es mejoir si estan ordenados de alguna forma, en este caso se agrupa por marca y se obtiene una cantidad que es guardado en **can** y se queiure ordenar a razón del valor **can** con el valor 1 se hace de forma *ASCENDENTE*

```javascript
db.automotor.aggregate([{$group: {_id:'$MARCA', can:{$sum:1}}}, {$sort:{can:1}}])
```
con -1 es descendente

```javascript
db.automotor.aggregate([{$group: {_id:'$MARCA', can:{$sum:1}}}, {$sort:{can:-1}}])
```

### Limit
Cuando se tienen bases de datos muy enormes puede que solo se quiera los primeros resultados y no todos los datos, para ello se da uso de este parametro. En el siguiente ejemplo se hace
* obtiener y agrupa por marca 
* por cada dato dato agrupado sumar 1 y guardarlo en una llave llamada can
* ordenar de forma descendente por ese valor can
* finalmente limitar la cantidad de resultados a 5 maximo

```javascript
db.automotor.aggregate([{$group: {_id:'$MARCA', can:{$sum:1}}}, {$sort:{can:-1}}, {$limit:5}])
```

# Tarea
Configurar una base de datos mysql en el servidor

https://www.digitalocean.com/community/tutorials/como-instalar-mysql-en-ubuntu-18-04-es

en caso de desintalar

https://linuxscriptshub.com/uninstall-completely-remove-mysql-ubuntu-16-04/

sudo apt-get remove --purge mysql* -y
sudo apt-get autoremove -y
sudo apt-get autoclean

instlaar pymongo 3.1.1

instalar sqlalchemy 1.3.20


# Terminos clave
aggregate -> ensamblaje
