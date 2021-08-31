import sys
# more SP1.csv | python mapftb.py | python reduccionftb.py
salida={}

# Agrupar los datos en algo especifico sobre sus mismas llaves 
# resultantes del mapeo

# sys.stdin gets all output from executon, example a pipe operation
for line in sys.stdin:
    line=line.strip()# Delete white spaces
    eqp, goles = line.split("\t")
    # print("Equipo {}, goles {}".format(eqp, goles))

    # Agrupation proces
    if eqp in salida: # eqp is not None
        salida[eqp].append(int(goles))
    else:
        salida[eqp]=[int(goles)]
    

print(salida)

# Reduction
goles_enum=0
# reducción es una agrupación de los datos
for eqp in salida:
    print(eqp, sum(salida[eqp]))