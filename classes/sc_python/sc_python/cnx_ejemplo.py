import luigi
import os

class Consulta(luigi.Task):
	def requries(self):
		return []

	def output(self):
		return luigi.LocalTarger("resultado.csv")

	def run(self):
		os.system('mongo < mazda.js')
		os.system('mongoexport --db=vehiculos --collection=automotor --type=csv --field= --out=resultado.csv')
