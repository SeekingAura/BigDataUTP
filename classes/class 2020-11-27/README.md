# Luigi
Fue desarrollado por Spotify

## Caracteristicas
* Gestión de dependencias

## Utilidad

* Monitoreo de tareas
* Transferencia de datos de un lugar a otro
* Automatizar operaciones de desarrollo
* Extraer datos de sitios web y llevarlos a bases de datos 
* Extraer datos de sitios web y llevarlos a bases de datos
* Procesamiento de datos en sistemas basados en recomendación
* Tuberias en modelos de aprendizaje de maquina

## Componentes basicos
* **Target** es el objetivo, en pocas palabras la definición de la salida del sistema, la cual puede ser a otro sistema o plataforma (HDFS, MongoDB, etc)

* **Task:** Es el lugar donde se realiza un trabajo o tarea, Una tarea peude ser dependiente o independiente, contiene los siguientes métodos:

* Requires(): Es el miembro de la función de la clase tarea que contiene todas las instnacias que deberán ser ejecutadas por la tarea actual
* output(): Este método contiene el objetivo al que apunta la salida que arrojará la tarea y que deberá ser almacenada. Puede contener uno o más objetivos
* Run()

## Requirements
* Python
* pip install luigi
* importar luigi

## Ejemplos
En luigi se puede hacer pipes o schedules de diferentes labores o tareas al mismo tiempo permitiendo multiples ejecuciones


### una tarea "simple"
```python
import luigi
# python ejemplo_luigi.py Cuadrados --local-scheduler

class SalidaNumeros(luigi.Task):
        def requires(self):
                return []

        def output(self):
                return luigi.LocalTarget("numeros.txt")

        def run(self):
                with self.output().open('w') as f:
                        for i in range(1, 11):
                                f.write("{}\n".format(i))
```

```python
class Cuadrados(luigi.Task)
        def requires(self):
                return [SalidaNumeros()]

        def output(self):
                return luigi.LocalTarget("cuadrados.txt")

        def run(self):
                with self.input()[0].open() as fin, self.output().open("w") as fout:
                        for line in fin:
                                n=int(line.strip())
                                val=
```python
class Cuadrados(luigi.Task):
        #n= luigi.IntParameter()
        n=luigi.IntParameter(default=10)

        def requires(self):
                return [SalidaNumeros(n=self.n)]

        def output(self):
```

### Ejemplo con mongo
```python
import luigi
from pymongo import *

class Ver(luigi.Task):
    nombd=luigi.Parameter()
    col=luigi.Parameter()
    ip='localhost'
    puerto=27017
    consulta={}


    def requires(self):
        return []

    def run(self):
        cliente=MongoClient(self.ip, self.puerto)
        db=cliente[self.nombd]
        coleccion=db[self.col]
        res=coleccion.find_one(self.consulta)
        print(res)

if __name__ == '__main__':
    consulta={}
    col=Ver(nombd='vehiculos',col='sumatoria')
    col.consulta=consulta
    col.run()
```


### Ejecutar en un host
Cuadrados es la tarea que se le asigna
python3 ejemplo_luigi.py Cuadrados --scheduler-host localhost --n 100000000