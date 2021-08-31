import os
import sys

print('Parametros recibidos: ', sys.argv)
print('Archivo a ejecutar: ', sys.argv[1])

archivos=sys.argv[1]
lista=archivos.split(',')

print('lista de programas a ejecutar; ', lista)

for archivo in lista:
	comando='mongo < ' + archivo
	os.system(comando)


