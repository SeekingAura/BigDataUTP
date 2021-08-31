# Map-reduce
Paradigma de programación de procesamiento de datos a gran escala sobre grupos de servidores.

Es un esquema de computación en paralelo que permite distribuir el trabajo entre diferentes máquinas.

Este presente en modelos distribuidos como hadoop, Google y Mongodb.

## Etapas
* **Mapeo:** Transforma el conjunto de datos de partida en pares (clave, valor) a otro conjunto de datos (clave, valor)

Un ejemplo de mapeo es "buscar" el dato que se desea obserbar en donde se encuentra el dato particular que tiene el conjunto de datos, por ejemplo en un CSV son separados por ', y por '\n' a razón de esto se separa los datos en bloques.

* **Reducción:** recibbe los valores intermedios procesados para agruparlos y producir un resultado.

Un ejempl de reducción Una vez el dato este separado mediante el proceso de mapeo y clasificado a razón de ese formato se juntan los datos que se repiten y se establece eso como una llave unica y se hace un "conteo" de esos

* Splitting: separar el conjunto de datos


En otras palabras, mapeo es el hecho de tomar un CSV y tomar a razón de las llaves una columna completa o bien identificar su etiqueta y tomar sus valores. O bien tomar una lalve y los vcalores de esa llave