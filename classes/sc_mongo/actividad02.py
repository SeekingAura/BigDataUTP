import os
import sys

print('Parametros recibidos: ', sys.argv)
print('Archivo a ejecutar: ', sys.argv[1])

archivo=sys.argv[1]
comando='mongo < ' + archivo

# print(comando)

os.system(comando)
