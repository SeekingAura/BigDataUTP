# Querys en mongo
Mongo tiene la capacidad de realizar de cierto modo consultas asi como se hace en SQL



## Renombrar llaves de los collections
Hay ocasiones que el nombre de la llave que tienen los datos no son muy adecuados para realizar operaciones en el (al momento de migrar los datos), para ello se realiza

```
db.COLLECTION.updateMany({}, { $rename: {"nombre anterior":"nombre nuevo"}})
```

## Buscar valores que sean menores a uno determinado y limitar resultado
```
db.automotor.find({MODELO:{$lt:2020}}).limit(5)
```

## DISTINC ROW 
Obtener todos los valores diferentes que tiene una llave en especifico
```
db.automotor.distinct('VEHICULO')
```

## Sorting results
En mysql seria agregar un ASC o DESC a razón de alguna Key. En este caso se obtendrá todos los vehiculos de marca **CHEVROLET** ordenado de forma **ASCENDENTE** dado por el número 1
```
db.automotor.find({MARCA:"CHEVROLET"}).sort({VEHICULO:1})
```

Para descendente en vez de 1 seria -1. Esta query es para ordenar del modelo mas reciente (más mayor) al mas viejo (más menor)
```
db.automotor.find({MARCA:"CHEVROLET"}).sort({MODELO:-1})
```

## Determinar que datos mostrar del resultado de algna query
Despues de la "," se puede indicar que datos mostrar o cuales no mostrar. Por ejemplo indicar que muestre PLACA y MODELO

```
db.automotor.findOne({}, {PLACA:1, MODELO:1})
```

Esto funciona para cualquier tipo de query de find, sin embargo cuando se indica cuales mostrar mediante el valor 1 siempre mostrará el _id, si se quiere quitar debe hacerse lo siguiente

```
db.automotor.findOne({}, {_id:0, PLACA:1, MODELO:1})
```

Para indicar cuales no mostrar es mediante el 0 como se hizo anteriormente, sin embargo, no se puede combinar 0 y 1 con las llaves diferentes al **_id** o todas son 0 o todas son 1. La siguiente query muestra todo Excepto placa y modelo

```
db.automotor.findOne({}, {PLACA:0, MODELO:0})
```

## Expresiones logicas AND, OR
Las expresiones logicas permiten el uso de mas condiciones, el uso mas habitual es establecer rangos o realizar rangos de busquedas

```
db.automotor.find({$and: [{ MODELO: {$lte: 2012}},{MODELO: {$gte : 2010}}]})
```

## Map Reduce
El mapeo y reducción permite indicar o establecer los datos para realizar conteos, tratamiento a los datos entre otros. El map reduce se logra mediante **scripts** en mongo y para ello deben de cierto modo "programarse" para ello debe realizarse con javascript guardando los scripts en variables

Recordemos que el mapeo es la operación del tomo de los datos y la reducción es el agrupamiento de los datos

### Conteo a razón de llave existente

```javascript
var map=function(){
    emit(this.VEHICULO, 1)
}
```

Con el script anterior hace que por cada que exista la llave VEHICULO va emitir el valor de 1.

Una reducción para sumar todos los valores encontrados la siguiente

```javascript
var reduce=function(llave, valor){
    return Array.sum(valor)
}
```

Ese script permite que cada que encuentre un valor en la llave vehiculo si es reptido se sumará, es decir si encuentra por segunda vez acumulará 1+1. Para ejecutar el mapReduce se debe usar lo siguiente
```javascript
db.automotor.mapReduce(map, reduce, {out:'sumatoria'})
```

Esta ejecución asi como está guardará en un collection de la DB actual con el nombre sumatoria

## Scritps equivalent to SQL
Elc ore de mongo es JavaScript por lo cual si se quieren hacer ejecuiones de querys ordenadas o comandos ordenados de sentencia ordenada se puede almacenar en archivos javascript tanto para las querys como para scripts complejos
