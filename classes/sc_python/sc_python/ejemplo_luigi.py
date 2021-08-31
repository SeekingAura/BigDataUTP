import luigi
import time

class SalidaNumeros(luigi.Task):
	n=luigi.IntParameter()
	def requires(self):
		return []

	def output(self):
		return luigi.LocalTarget("numeros_{}.txt".format(self.n))

	def run(self):
		with self.output().open("w") as f:
			for i in range(1, self.n+1):
				f.write("{}\n".format(i))


class Cuadrados(luigi.Task):
	n=luigi.IntParameter(default=10)
	def requires(self):
		return [SalidaNumeros(self.n)]

	def output(self):
		return  luigi.LocalTarget('cuadrados_{}.txt'.format(self.n))

	def run(self):
		with self.input()[0].open("r") as f_in, self.output().open('w') as f_out:
			for line in f_in:
				n=int(line.strip())
				val=n*n
				f_out.write("{}:{}\n".format(n, val))

if __name__ == '__main__':
	luigi.run()
