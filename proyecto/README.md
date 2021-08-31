# Fuente de datos
https://www.datos.gov.co/Justicia-y-Derecho/Conteo-de-Indiciados/37ii-v4q2

# CSV download
https://www.datos.gov.co/api/views/37ii-v4q2/rows.csv?accessType=DOWNLOAD


count = sum(1 for _ in f)
        print("Total de saltos de linea", count)



python3 getdata.py Extract_data --local-schedule --file-read conteo_indiciado.csv --perc 0.01




mongoimport --db indiciados --collection sample_001 --type=csv --file sample_0-01.csv --headerline


indiciados

sample_001



db.sample_001.aggregate([{$match:{$and:[{DEPARTAMENTO:"Risaralda"}, {MUNICIPIO:"PEREIRA"}]}}]);
# db.sample_001.aggregate([{$match:{$and:[{DEPARTAMENTO:"Risaralda"}, {MUNICIPIO:"PEREIRA"}]}}])

python3 getdata.py Get_stadistics --local-schedule --file-read conteo_indiciado.csv --perc 0.01 --db indiciados --filters '[{"$match":{"$and":[{"DEPARTAMENTO":"Risaralda"}]}}]' --analytic LEY

python3 getdata.py Get_stadistics --local-schedule --file-read conteo_indiciado.csv --perc 0.01 --db indiciados --filters '[{"$match":{"$and":[{"DEPARTAMENTO":"Risaralda"}, {"MUNICIPIO":"PEREIRA"}]}}]' --analytic LEY

python3 getdata.py Get_stadistics --local-schedule --file-read conteo_indiciado.csv --perc 0.01 --db indiciados --filters '[{"$match":{"$and":[{"DEPARTAMENTO":"Risaralda"}, {"MUNICIPIO":"PEREIRA"}]}}]' --analytic ANIO_ENTRADA

python3 getdata.py Get_stadistics_and_sql --local-schedule --file-read conteo_indiciado.csv --perc 0.01 --db indiciados --filters '[{"$match":{"$and":[{"DEPARTAMENTO":"Risaralda"}, {"MUNICIPIO":"PEREIRA"}]}}]' --analytic ANIO_ENTRADA

python3 getdata.py Get_stadistics_and_sql --local-schedule --file-read conteo_indiciado.csv --perc 0.01 --db indiciados --filters '[{"$match":{"$and":[{"DEPARTAMENTO":"Risaralda"}, {"MUNICIPIO":"PEREIRA"}]}}, {"$project" :{"_id":0}}]' --analytic ANIO_ENTRADA

analytic=luigi.Parameter()
stadistic_result_file=luigi.Parameter()

# Mysql
show schemas;
use mongo_results;

DESCRIBE table_name;
EXPLAIN table_name;

## Keys
HECHO,RUPTURA,CONEXO,ESTADO_NOTICIA,ETAPA,ANIO_DENUNCIA,ANIO_ENTRADA,ANIO_HECHO,LEY,PAIS,DEPARTAMENTO,MUNICIPIO,SECCIONAL,GRUPO_DELITO,DELITO,IMPUTACION,CONDENA,ATIPICIDAD_INEXISTENCIA,ACUSACION,CAPTURA,SEXO_INDICIADO,GRUPO_EDAD_INDICIADO,PAIS_NACIMIENTO,HOMICIDIO_DOLOSO_CONSUMADO,TOTAL_INDICIADOS

SET GLOBAL local_infile=1;

## Tomar un archivo
scp mongo@18.223.206.199:"proyecto/result/Histogram.png" Histogram.png

## Enviar un archivo
scp getdata.py mongo@18.223.206.199:/home/mongo/proyecto