# 



```python
import luigi
#python3 muestra.py Muestra --local-schedule --info '{"origen":"victim_count.csv"}'
#python3 muestra.py Muestra --local-schedule --info '{"origen":"victim_count.csv"}' --limite 20

class Muestra(luigi.Task):
        info=luigi.DictParameter()
        limite=luigi.IntParameter(default=10)

        def requires(self):
                return []

        def output(self):
                return luigi.LocalTarget("muestra_{}.csv".format(self.limite))


        def run(self):
                archivo_origen=self.info['origen']
                with open(archivo_origen, "r") as origen, self.output().open("w") as destino:
                        for con, l in enumerate(origen):
                                linea=l.strip()#Removes extra spaces and tabs
                                destino.write(linea+'\n')
                                if con >= self.limite:
                                        break

if __name__ == "__main__":
        luigi.run()
```


```bash
mongoimport --db fiscalia --collection victimas --type=csv --file muestra_10.csv --headerline
```

## Funcionamiento de luigi

Luigi funciona ejecutnado de lo ultimo hacia atras, esto cuando se hace el uso de "pipelines", ahora para darle sentido a luigi se realizará el siguiente proceso que es el comando para migrar a mongo

```python
import luigi

#python3 proceso.py MigrarMongo --local-schedule --info '{"origen":"victim_count.csv"}'
#python3 proceso.py MigrarMongo --local-schedule --info '"origen":"victim_count.csv"' --limite 20

class Muestra(luigi.Task):
        info=luigi.DictParameter()
        limite=luigi.IntParameter(default=10)

        def requires(self):
                return []

        def output(self):
                return luigi.LocalTarget("muestra_{}.csv".format(self.limite))


        def run(self):
                archivo_origen=self.info['origen']
                with open(archivo_origen, "r") as origen, self.output().open("w") as destino:
                        for con, l in enumerate(origen):
                                linea=l.strip()#Removes extra spaces and tabs
                                destino.write(linea+"\n")
                                if con >= self.limite:
                                        break

class MigrarMongo(luigi.Task):
        info=luigi.DictParameter()
        limite=luigi.IntParameter(default=10)
        def requires(self):
                return [Muestra(info=self.info), limite=self.limite]

        def output(self):
                return []

        def run(self):
                os.system("mongoimport --db fiscalia --collection victimas --type=csv --file {} --headerline".format("muestra_{}.csv".format(self.limite)))



if __name__ == "__main__":
        luigi.run()
```

En este script se realiza primero la muesra y luego se ejecuta el **MigrarMongo**


Ahora un script para ejecutar de mongo de filtrar por cada muestra, primero se crea un js con lo siguiente:
```javascript
use fiscalia
db.victimas.aggregate([{$match:{SEXO_VICTIMA:"FEMENINO", DEPARTAMENTO:"Risaralda"}}, {$out:"femenino"}])
```






# Research and Development != Engineering


# Pipelines

# Premisas para la ingenieria de datos
* Your data is dirty unless proven otherwise - Sus datos estan sucios hasta que se demeustre lo contrario  
* Que esten en una base de datos No quiere decir que sean buenos o esten limpios
* Todos los datos son importantes, no deberian ser omitidos. Mantengalos


## Pipes vs scripts soup

Una sopa de scrips es varios scripts que sirven para multiples funciones, el problema es que **NO SON BUENOS** Para la replicabilidad.



# Proyectos
* Diseño e implementación de un proyecto de base de datos NoSQL
Generar un sistema analitico de forma automatica: es decir que permita analisis pasados por parametro

Automatización: Lanzar programa o aplicación que genere el producto de datos.

**Bajo:** No genera extracción  
**Aceptable:** Generar el producto de una o varias collecciones sin automatización. Hay scripts que generan las colecciones pero se requiere ejecutar cada una para obtener el producto (ejemplo: el script el que genera Victimas femeninas de risaralda en colección, conteo de delitos, victimas entre 2016 a 2020)  
**Competente:** Ejecuto un programa que articula y genera colecciones desde un solo archivo, ademas de conectarlo con un sistema analitico (medidas de tendencia central media, mediana, moda, desviación estandar, histograma)

**Excelente:** Ejecuto un programa que articula y genera colecciones desde un solo archivo, ademas de conectarlo con un sistema analitico y generar estadisticos basicos y prueba de hipotesis


Generar en el sistema que genere una prueba estadistica donde muestre la media, mediana, moda


* Diseño de e implementación de un proyecto de base de datos SQL, partiendo de que los datos estan en la base de datos de mongo

Se debe pasar un conjunto de datos (llaves) al SQL.

**Bajo::** No migras datos de modelo NoSQL a SQL  
**Aceptable:** migras del modelo NoSQL al modelo SQL empleando varios scripts de migración  
**Competente:** Ejecutar un programa que articula y genera las tablas apartir de una colección creada a partir de los datos crudos al modelo SQL

**Excelente:** Ejecuta un programa que articula y genera las tablas cradas a partir de los datos rudos al modelo SQL y ademas lo conectas con sistema analitico y generas estadisticos basicos


