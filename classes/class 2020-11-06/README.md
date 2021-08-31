# Mas acerca de modelos de bases de datos

## Implicaciones del modelo ACID
* Las bases de datos NoSQL prescinden del ACID para privilegiar tolerancia o disponibilidad

* ACID: Atomicity, Consistency, Isolation, Durability -> Atomicidad, consistencia aislamiento y durabilidad
* **Atomicidad:** Se ejecuta todo o nada
* **Consistencia:** Coherencia de los datos
* **Aislamiento:** Transacciones independientes entre si
* **Durabilidad:** Persiste aun que falle el sistema
* Escalabilidad y velocidad se resisten

# Modelo BASE
La alternativa del modelo ACID es el BASE

* Basically Available, Soft state, Eventually consistent.
* Basically(B) Avaliable (A): disponible aún cuando ocurran fallos, una parte accesible al menos
* Soft (S) state: la información puede ser bolátil y no mantener consistencia
* Eventually (E) consistent: la información se propagará en los nodos garantizando consistencia en álgun momento 

# Usos de NoSQL
* Amazon: Dynamo, es una base de datos propia de ellos donde se realizó un sistema en donde se garantiza consistencia para que no  se repitan los datos y se tenga el acceso correspondiente
* Google: Big table, es una base de datos que permite datos repetidos en los repetidos y multiples datos conectados
* Facebook: Cassandra, Esta base de datos es tipo Grafo que se hizo acorde a las necesidades que se tenian en su momento
* Twitter: FlockDB, Las necesidades de twiter es los enlaces y el como se conectan los mensajes o bien olos "tweets" que se forman en este sistema
* LinkedIn: Voldemort

El uso de tecnologias propias está ligado a las restricciones y cambios que haga el dueño o creador del kernel

# Bases de datos NewSQL
* Bases de datos relacionales que tratan de igualar el rendimiento de la sbases de datos NOSQL mantenimiento las garantías de **ACID**
* Algunas de ellas son MariaDB, CockroachDB, WebScale

# MongoDB

## Elementos basicos
* **Database:** Es un contenedor físico para las colecciones. Cada base de datos obtiene su propio conjunto de archivos
* **Collection:** Es un grupo de documentos de MongoDB. Es el equivlaente a una tabla RDBMS. Una colección existe de una sola base de datos. Las colecciones no poseen un esquema, los documentos dentro de una colección pueden tener diferentes campos.
* Document: Es un conjunto de pares clave-valor. Los documentos tienen un esquema dinámico, lo qeu significa que los documentos en una misma colección no necesitan tener el mismo conjunto e campos o estructura y los campos comunes en los documentos de una colección pueden tener diferentes tipos de datos.

## Instalación de mongo
