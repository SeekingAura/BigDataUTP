import sys
# more SP1.csv | python mapfutbol.py
# Mapeo es el proceso de tomar los valores a razón de las llaves

try:
    # file_data=open()
    for enum, line in enumerate(sys.stdin):
        if(enum==0):
            continue
        line=line.strip()# Delete white spaces
        ls=line.split(',')
        print("{}\t{}".format(ls[3], ls[5])) # Map is take from specific key, here takes from key index 3 and 5
except:
    print("Error")