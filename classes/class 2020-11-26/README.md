# Acceso temporal para mysql.

En la configuración que se hizo la semana pasada para ingresar debe ejecutar lo siguiente

```bash
sudo mysql -uroot -p
```

## Verificar estado del servicio
```
systemctl status mysql.service
```

## Comandos en mysql

### Mostrar bases de datos o schemas que en la maquina
```sql
show databases;
```

### Selelecionar una base de datos o schema en especifico
```
use sqlejemplo;
```

### Mostrar las tablas que contenga una base de datos (la que se tenga seleccionada)
```
show tables;
```

### Mostrar base de datos seleccionada actualmente
```sql
SELECT DATABASE();
```

### Mostrar detalles de una tabla en especifico
```sql
DESCRIBE orders;
```

### Crear usuarios
```sql
CREATE USER 'user'@'hostwhereconnect' IDENTIFIED BY 'password';
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'Bigdata-2020';
```

### Dar permisos a users
https://phoenixnap.com/kb/how-to-create-new-mysql-user-account-grant-privileges
```sql
GRANT ALL PRIVILEGES ON *.* TO 'database_user'@'localhost';
```

### Mostrar politica de contraseñas
```sql
SHOW VARIABLES LIKE 'validate_password%';
```

### Modificar politicas de contraseña a nivel LOW
```sql
SET GLOBAL validate_password.policy=LOW;
```

## Tipos de dato int
```
TINYINT = 1 byte (8 bit)
SMALLINT = 2 bytes (16 bit)
MEDIUMINT = 3 bytes (24 bit)
INT = 4 bytes (32 bit)
BIGINT = 8 bytes (64 bit).
```
# python y msql

## Instalar Librerias

### sqlalchemy
```python
pip install sqlalchemy
```

### dialecto para mysql trabjar con salalchemy
Esto es extrido de esta web https://docs.sqlalchemy.org/en/14/dialects/index.html solo es necesario instalar 1 solo de lo dialectos para el manejador de base de datos
```
pip install pymysql
```

## Ejemplos de código fuente


### Conectar al mysql
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Connect to db
# motor=create_engine('tipodb+dialecto://usr:pw@ip:puerto/basedatos')
motor=create_engine('mysql+pymysql://admin:Bigdata-2020@localhost:3306/sqlejemplo')

# Definition about sesion
Session = sessionmaker(bind=motor)

# Login to database
sesion = Session()

# Definition about library base
Base=declarative_base()
```

### Crear una tabla
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey

# Connect to db
# motor=create_engine('tipodb+dialecto://usr:pw@ip:puerto/basedatos')
motor=create_engine('mysql+pymysql://admin:Bigdata-2020@localhost:3306/sqlejemplo')

# Definition about sesion
Session = sessionmaker(bind=motor)

# Login to database
ssesion = Session()

# Definition about library base
Base=declarative_base()

class Usuario(Base):
        __tablename__= 'usuarios'
        id=Column(Integer, primary_key=True)
        descripcion=Column('descripcion', Text)
        activo=Column(Boolean)
        edad=Column(Integer)

Base.metadata.create_all(motor)
```


### Insertar datos a una tabla
Esta insersión se basa en la estructura de la tabla usuario dada en ejemplo anterior. se crea la tabla y luego se inserta un dato

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, Boolean, ForeignKey

# Connect to db
# motor=create_engine('tipodb+dialecto://usr:pw@ip:puerto/basedatos')
motor=create_engine('mysql+pymysql://admin:Bigdata-2020@localhost:3306/sqlejemplo')

# Definition about sesion
Session = sessionmaker(bind=motor)

# Login to database
ssesion = Session()

# Definition about library base
Base=declarative_base()

class Usuario(Base):
        __tablename__= 'usuarios'
        id=Column(Integer, primary_key=True)
        descripcion=Column('descripcion', Text)
        activo=Column(Boolean)
        edad=Column(Integer)

Base.metadata.create_all(motor)

usr=Usuario(descripcion='jugador 1', activo=True, edad=20)
session.add(usr)
session.commit()
```

### realizar query de SELECT en los datos

#### Obtener el primer dato en la tabla
```python
con1=db.session.query(Usuario).get(1)
print(type(con1), con1.id, con1.descripcion)
```

#### Obtener TODOS los datos de una tabla

```python
con2=db.session.query(Usuario).all()

for u in con2:
        print(u.id, u.descripcion)
```

#### Obtener la cantidad de datos de una tabla

```
con3=db.session.query(Usuario).count()
print("cantidad de registros", con3)
```

#### Realizar una query en una tabla con condiciones especificas (WHERE)

```python
con4=db.session.query(Usuario).filter(Usuario.id==1)
print(con4)
```

for u in con4:
        print(u.id, u.descripcion)

```

# Tareas
1. Proxima semana quiz a razón de diapositivas
2. Archivo de extraer cinjuntos de variables de analisis
3. programa integre la ETL (datos, transición o insersión)
4. Articulo (No se evalua)
