# Multiples servicios en la maquina
El hadoop contiene un sistema de archivos que esta en un servidor. Recordando el sitema de archivos hay servidores o otras maquinas que gestionan los archivos.

Los servicios en hadoop funcionan al estilo procesos, por lo cual tienen su funcionamiento de manera independiente. En ese caso en el servidor hadoop se correran varios servicios al mismo tiempo, en este caso estará el servicio de Hadoop y el Yarn al mismo tiempo

# Install hadoop
* Para instalar hadoop primero se descarga

wget https://downloads.apache.org/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz

* luego se descomprime
```
$ tar -xvzf hadoop-3.2.1.tar.gz
```
* Ahora si se queire para que lo utilice todos los usuarios se colocará en /usr/local
```
$ sudo mv hadoop-3.2.1 /usr/local/hadoop
```
* Creamos una carpeta logs dentro del hadoop
```
$ sudo mkdir /usr/local/hadoop/logs
```
* Le damos permisos del usuario a toda la carpeta y a los usuarios a los del grupo
```
$ sudo chown -R hadoop:hadoop /usr/local/hadoop
```

# En .bashrc del usuario hadoop colocar al final
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






