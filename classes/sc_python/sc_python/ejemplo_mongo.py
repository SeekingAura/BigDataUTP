import luigi
from pymongo import *

class Ver(luigi.Task):
    nombd=luigi.Parameter()
    col=luigi.Parameter()
    ip='localhost'
    puerto=27017
    consulta={}


    def requires(self):
        return []

    def run(self):
        cliente=MongoClient(self.ip, self.puerto)
        db=cliente[self.nombd]
        coleccion=db[self.col]
        res=coleccion.find_one(self.consulta)
        print(res)

if __name__ == '__main__':
    consulta={}
    col=Ver(nombd='vehiculos',col='sumatoria')
    col.consulta=consulta
    col.run()
