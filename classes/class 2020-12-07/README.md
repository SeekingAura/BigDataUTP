# Resumen mongo

## Llevar un archivo del local al servidor
```bash
scp prod_cacao_dpt.csv mongo@3.129.217.70:/home/mongo/repo/prod_cacao_dpt.csv
```

## importar de un archivo a mongo
```bash
mongoimport --db nombre_db --collection nombre_collection --type=csv --file nombre_archivo --headerline
mongoimport --db Cultivos --collection Cacao --type=csv --file prod_cacao_dpt.csv --headerline
```

# Comandos mongo

## Obtener todos los valores diferentes dado una llave
```javascript
db.Cacao.distinct("DEPARTAMENTO")
```

## Agrupar por una llave n especifico y colocarlo como otra llave en especifico
```javascript
db.Cacao.aggregate([{$group: {_id:"$DEPARTAMENTO"}}])
```

## Agrupar por una llave n especifico y colocarlo como otra llave en especifico y guardar el resultado en un collection
El resultado se guarda en el collection Departamentos
```javascript
db.Cacao.aggregate([{$group:{_id:"$DEPARTAMENTO"}},{$out:"Departamentos"}])
```

En este caso agrupa por la llave departamento y lo asigna como "_id", la lalve _id es la que usa mongo como identificador unico