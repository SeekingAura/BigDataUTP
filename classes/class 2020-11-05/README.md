# Utilizando hadoop

## Inicializar el servicio de sistema de archivos
```
$  start-dfs.sh
```

## Inicializar el servicio de scripts de hadoop el yarn
```
start-yarn.sh
```

## Inicalizar todos los servicios de hadoop
La siguiente instrucción ejecuta todos los servicios del hadoop
```
start-all.sh
```

## Abrir los puertos

### Namenode
Acceder a la información general del hadoop y herramientas
**TCP 9870**

### Datanodes
Acceder a la información general de los bloques y nodos de datos
**TCP 9864**

### Job Tracker
Acceder a las tareas y los procesos que está ejecutnado el hadoop
**TCP 8088**
### node info
8042


## herramientas de hadoop
en el Namenode acceder a *Utilities/Browse the File system*, En la carpeta *$HADOOP_HOME/bin* se encuentran los comandos de hadoop y alli hay varias herrmaientas que se pueden usar en la terminal
### Commando hdfs
```
$HADOOP_HOME/bin/hdfs dfs
```

hdfs dfs invocan comandos tipicos del sistema operativo

Este lista os archivos del dfs

### Comando ls
```
$HADOOP_HOME/bin/hdfs dfs -ls /
```
Listar los archivos del sistema de archivos de hadoop


### Comando mkdir
```
hdfs dfs -mkdir /prueba
```

Crear una carpeta en la raiz del sistema de archivos hadoop

### Colocar un archivo especifico que hay en la maquina al sistema de archivos de hadoop
Copiar el archivo *D1.csv* En */prueba/D1.csv* al sistema de archivos de hadoop
```
hdfs dfs -put D1.csv /prueba/D1.csv
```


# No-sql
Not Only SQL: Modelos de b ases de datos que apareecen como respuesta a los problemas encontrados en las bases de datos relacionales, principalmente de escalamiento.

## Modelos SQL y no SQL
El modelo SQL conserva una estructura rigida lo cual se predefine los valores que han de existir para lo datos.

El modelo No-SQL en sus inicio fue basado en documentos el cual se tiene registros de información que pueden tener llaves de manera dinamca.

## Ventajas No SQL
* Requiere pocos recuros
* Escalabilidad horizontal
* Manejan gran cantidad de recursos

## Diferencias del NoSQL contra el SQL
* No usan SQL como lenguaje de consultas
* No usan estructuras fijas de almacenamiento tales como tablas
* No suelen usar operaciones tipo JOIN
* Arqutiectura distribuida

## Tipos de bases de datos No SQL
* Bases de datos clave valor
* Bases de datos documento JSON o XML
* Bases de datos grafos
* Bases de datos orienado a objetos

## Modelo CAP
* **Consistency:** Los datos son facilmente identificables
* **Aviability:** Accesibilidad a los datos
* **Partition Tolerance:** Escalabilidad

* Las bases de datos SQL cumplen con *Consistency y Abailability*
* Las bases de datos no SQL tipo archivo son *Consistency y Partition tolerance*
* La base de datos de google (big table) para los motores de busqeuda cumple con *Avaliability y Partition tolerance*. un ejemplo claro de que se cumple con eso es uqe cuando se hace una busqueda sale veces datos repetidos haciendo que los datos no sean consistentes lo cual eso no importa.

Las bases de datos no pueden tener las 3 caracteristicas al tiempo por lo cual siempre tienen a lo sumo 2 de las 3. Hadoop trata de cumplir con estos sin embargo, el problema uqe tiene hadoop es con la Aviability siendo un modelo CP debido a que tien e los datos de forma distribuida su aviability es afectado.

# tarea
Buscar la base de datos mas grande que se pueda encontrar y que sea descargable
