# Install hadoop
## Para instalar hadoop primero se descarga

wget https://downloads.apache.org/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz

## luego se descomprime
```
$ tar -xvzf hadoop-3.2.1.tar.gz
```
## Ahora si se queire para que lo utilice todos los usuarios se colocará en /usr/local
```
$ sudo mv hadoop-3.2.1 /usr/local/hadoop
```
## Creamos una carpeta logs dentro del hadoop
```
$ sudo mkdir /usr/local/hadoop/logs
```
## Le damos permisos del usuario a toda la carpeta y a los usuarios a los del grupo
```
$ sudo chown -R hadoop:hadoop /usr/local/hadoop
```

## En .bashrc del usuario hadoop colocar al final
```
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"
```

## Determinar donde esta JAVAC
* detemrianr odnde esta el java
```
    $ which javac
    /usr/bin/javac
```
* generlamente en los sistemas linux tiene un sistema de accesos directos es decir en usr/bin no estan los sistemas directos alli o bien en algunos casos son scripts enlazados al fichero de funcinamiento, por lo cual toca descubrirlos mediante **readlink**
```
    $ readlink -f /usr/bin/javac
    /usr/lib/jvm/java-11-openjdk-amd64/bin/javac
```
 
## Contenido de ls ficheros de haddop
### bin
En bin están los scripts de hadoop, com tal está todo el sistmea de comandos

### etc

### include
funciones que utiliza hadoop para sus procedimientos

#### Native
Archivos para procesar a hadoop, en si es el core de hadoop

### libexec
Comando s de configuración de hadoop

### sbin
Instrucciones para lanzar los servicios de hadoop

### share
Es el espacio que utiliza hadoop para realizar intercambio con los nodos


## Configurar hadoop
### Configurarle javac
modificar el script de enviroment, siendo el javac que encontramos antes
```
    $ nano /usr/local/hadoop/etc/hadoop
```

al final de archivo agregarle la variable para que haddop encuentre el java
```
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export HADOOP_CLASSPATH+=" $HADOOP_HOME/lib/*.jar"
```



## Configurar javax
En si es solo descargarlo en la carpeta lib de hadoop
```
cd /usr/local/hadoop/lib
sudo wget https://jcenter.bintray.com/javax/activation/javax.activation-api/1.2.0/javax.activation-api-1.2.0.jar
sudo chown -R hadoop:hadoop javax.activation-api-1.2.0.jar
```


## Configurar el core de hadoop
Editar la configuración de hadoop para que conozca donde tendrá el sistema de archivos

```
    sudo nano $HADOOP_HOME/etc/hadoop/core-site.xml

    <configuration>
    <property>
    <name>fs.default.name</name>
    <value>hdfs://0.0.0.0:9000</value>
    <description>Sistema de archivos por defecto URI</description>
    </property>
    </configuration>
```

## Configurar el site de hadoop
En este se configura el como funciona el sistema de archivos
```
sudo nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>

    <property>
        <name>dfs.name.dir</name>
        <value>file:///home/hadoop/hdfs/namenode</value>
    </property>

    <property>
        <name>dfs.data.dir</name>
        <value>file:///home/hadoop/hdfs/datanode</value>
    </property>
</configuration>
```

En este caso la configuración se hace 1 soa replicación ya que en un principio será un hadoop aislado (una sola maquina)

## Configurar carptas de HDFS
Primero hay que crear las carpetas del sistema de archivos
```
sudo mkdir -p /home/hadoop/hdfs/{namenode,datanode}
sudo chown -R hadoop:hadoop /home/hadoop/hdfs/
```


## Configurar el mapredside
Esto es para configurar el yarn en hadoop

```
sudo nano $HADOOP_HOME/etc/hadoop/mapred-site.xml

<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
```


## Configurar el yarn

```
sudo nano $HADOOP_HOME/etc/hadoop/yarn-site.xml

<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
</configuration>
```

# Inicializar hadoop
## inicializar la configueración el sistema de archivos
hdfs namenode -format

## Iniciar el Datafile system
start-dfs.sh

## Iniciar el gestor de recursdos YARN
start-yarn.sh



## Detener el hadoop
stop-all.sh

