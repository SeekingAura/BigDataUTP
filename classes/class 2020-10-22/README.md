# Big data management
1. Hadoop
2. HDFS
3. MapReduce
4. Sqoop
5. Flume
6. Kafka
7. NoSQL
8. HBase

Actualmente exisen muchas formas para gestionar muchos datos

## Hadoop
Es un sistema de apache, es una plataforma para el manjo de información distribuida y procesa sets de datos muy grandes en clusters de computadoras desde la comodidad del hardware. Los servicios de Hadoop provee almacenamiento de los datos, procesaaiento de datos, acceso a los datos, gobernamiento de los datos, seguridad y operaciones

El clustering está diseñado para tomar muchas maquinas pequeñas y de cierto modo "combinar" sus capacidades para que todas funcionen como una "super computadora", esto facilita la reutilización de recursos de bajo costo y que ademas suele ser mucho mas barato varias maquinas donde la suma de sus capacidades es igual a una super maquina.

Otra ventaja uqe tiene los sistemas clustering es que muy facilmente permite escalamiento

**Escalamiento horizontal:** hace referencia al crecimiento de *todo el sistema* es decir agregar maquinas a todo mi sistema (visto como el cluster) 

**Escalamiento vertical:** hace eferencia al crecimiento de *uno de los componentes* como aumentar disco, ram

### Hadoop History
Los inicios de hadoop inicia desde el sistema de archivos de google el cual fue publicado el 2003. Esa investigación generó otra investigación sobre el **mapReduce** es la simplificación del procesamiento de datos en clusters grandes. 

Los systemas de MySQL y oracle no están diseñados para funcionar en forma cluster, entonces Hadoop

### Beneficios de hadoop
Algunas razones por las que una organiozación utilice hadoop es la habilidad el almacenamiento, manejo de datos, analisis de montones de datos estructurados y no estructurados.

* **Escalibidad y rendimiento:** Procesamiento de datos distribuidos de forma local por cada nodo en un cluster permite a hadoop almacenamiento, mano procesamiento y analisis de datos a escalamiento de petabytes
* **Confiabilidad:** 
* **Flexibilidad**
* **Bajo costo**

### Hahoop: ecosystem
* **YARN:** distribuye las tareas y trabajos
* **Map Reduce v2:** Es el manejo de los datos de hadoop en el sistema
* Pig es el manejo de scripts
* Hive: limpia los datos
* Sqoop: permite la migración de datos de manera transparente
* Flume: Agente que se pone a "capturar" datos a razón de unas coniciones

### Haddop: arquitectura
funciona similar a un cliente servidor, el cual consta de lo siguiente
* un **main Node** el cual gestiona todos los procesos, servicios de las demas maquinas que conforman el sistema. Este nodo tambien es donde el cvliente hace la comunicación para realizar las tareas
* Job Tracker: es el servicio que se encarga de delegar trabajos


### Hadoop HDFS Arquitectura de cluster maestro esclavo
En el manejo de archivos cuando se va a almacenar se un archivo este es divido en diferentes partes y se **reparte** en diferentes servidores que conforman el sistema que tiene el hadoop, el sistema hadoop se encarga tambien de hacer "replicas".

Si llega a pasar que alguno de los trabajadores llega a fallar los demas trabajadores pueden seguir almacenando y funcionando con normalidad. El nodo principal contiene las direcciones y los registros de donde están los archivos. Esto queire decir que si el principal se muere el sistema quedado perdido.

En caso de haya alguna interrupción en el sistema los registros uqe maneja hadoop permite recuperarse.

Hadoop **NO** Es un sistema de almacenamineto y persistencia esto quiere decir que el sistema hadoop es **UNICAMENTE** para realizar tratamiento a los datos, analisis y obtener resultados.

## HDFS (Hadoop Distributed File System)
HDFS es un sistema de archivos basado en java, el cual es escalabl, confiable de almacenamiento y diseñado para esparcirse en un monton de clusteres.

Hadoop, esta diseñado más para datos instantaneos es decir cuando se suben los datos deben ser procesados y hasta que no termine de ser procesados no permite el ingreso de mas datos.

HDFS es escalable, tolerante a fallas, almacenamiento distribuido, los trabajos son precisos con una varidad de ocurrencia de aplicaciones de los datos.

Mediente el almacenamiento y computación distribuida entre varios servidores, combinan sus recursos de almacenamiento y puede crear linealmente con la demanda.

### HDFS Caracteristicas
* Se pueden colocar mas maquinas se ahora espacio
* Reducción en el movimiento de los datos
* Utilidad
* Rollbacks
* NameNode estable
* Operabilidad
* Alto crecimiento

### HDFS Arquitectura
El cliente envia la información al namenode, Se forma los metadados de como esrán repartidos. Luego se encarga de forma automatica entre los exclavos de repartirlo y de hacer a su vez la "replica"

### HDFS Namenode
El nodo principal de hadoob es este donde se tiene la información de como estan repartidos los datos y si este muere el sistema cae

### HDFS datanode
Son los nodos que estan dispuestos a almecanmiento de los datos y a su vez monitorea si el servidor principal está funciona (Keep alive)

### HDFS Secondary NameNode
Es el responsable del rendimiento del sistema, este tiene el funcionamiento de hacer checkpoints del sistema de archios y de los procesos que se estan realizando. En caso de falla del sistema los checkpoints formados por el Secondary NameNode son utilizados para reponerse.

### HDFS: Block placement policy
La politica de como se dividen los datos es tomar el dato y se divide en varios bloques donde es repartido en varias maquinas y se forma a su vez una *replica* de los fdatos el cual se lleva a otros esclavos para que asi si algun nodo falla se tiene aun la forma de construir el dato


### HDFS: block placement policy

### HDFS: Write

## MapReduce
Es el encargado del procesamiento de grandes datos el cual se encarga de convertir el dato en un set de datos con llaves y valores que permiten determinar el orden de los datos.

Mapreduce hace dos tareas como tal, el primero es mapear los datos donde se convierte un dato en un set de datos y se tiene el conteo donde da a conocer su orden.

La otra tarea que es reducir, la salida del dato es la construcción de los datos de como estna separados que permitan combinarse luego.

### MapReduce Beneficios
* **Simplicidad:** Es sencillo de realizar ya que es programable par alos lenguajes de programación comun como c++ y python
* **Escalable** MapReduce puede procesar Petabytes de datos y almacenarlo en un cluster de HDFS
* **Velocidad:** Prcesamiento paralelo (dado que se separa los archivos en partes es una facilidad de ello)
* Recuperación
* Minimal data motion


### Mapreduce arquitectura
* Job: Es un proceso que se ejecuta donde se incluye el mapeo, las entradas y los reductores para cruzar la salida del dataset
* Task: Cada trabajo está dividido entre varios mapeos y reducción. Una porción del trabajo es ejecutado en una parte de los datos la cual hace referencia como una tarea
* JobTracker: es el nodo maestro que maneja todos los jobs y recursos en el Hadoop cluster
* TaskTracker: es los agentes que estan en cada maquina del cluster para correr el mapeo y reducción y reportne el estado al jobtracker luego de su ejecución

En si lo que se hace ante los "jobs" que puede tener el sistema de hadoop es distribuir los recursos yt tareas a realizar en el sistema para llegar a un resultado. Todo depende de la tarea a realizar. En caso de que algun proceso falle este es reasignado.

### MapReduce: Flow
1. Un cliente carga jobs al JobTracker
2. El JobTracker obtiene información del NameNode de donde está la información en que Datanodes. El jobTracker toma lugar en el cliente para programar en un HDFS. Una vez el JobTracker empeuice a asignar tareas el TaskTracker empieza a dar operación sobre los Datos
5. Al completar las tareas de mapeo

### Mapreduce MR1 vs MR2
* MapReduce 1 "clasico" tiene tres componmente sprincipales
    * Una API para el usuario

* MapReduce 2 "NExtstep.. YARN"
    * El sistema de almacenamiento cuenta con otro sistema intermedio para llegar al control de los datos
    * Cada uqe se agregaba un componente era necesario que las maquinas se conecen de forma directo entre los sistemas

## Hadoop V3.
En este sistema hay una "capa" de la aplicación que facilita la amplicación de los equipos o la conexión de nuevos equipos (respecto a versioens anteriores). En esta versión se cuenta con un auto-balaceo de cargas lo cual en las versions anteriores era algo manual.


# AWS system
Los alquiler de serviciso de maquinas virtuales