import luigi
import os
from pymongo import *

import pandas as pd

from matplotlib import pyplot as plt

import numpy as np

folder="result"

# If does'nt exit create
if(not os.path.isdir(folder)):
	os.mkdir(folder)

def reservoir_sampling(l, k):
    it = iter(l)
    try:
        result = [next(it) for _ in range(k)] # use xrange if on python 2.x
    except StopIteration:
        raise ValueError("Sample larger than population")

    for i, item in enumerate(it, start=k):
        s = random.randint(0, i)
        if s < k:
            result[s] = item

    random.shuffle(result)
    return result

class Get_Var_numbers(luigi.Task):
	file_read=luigi.Parameter()

	def requires(self):
		return []

	def output(self):
		return luigi.LocalTarget("{}/count_{}".format(folder, self.file_read.replace(".csv", ".txt")))

	def run(self):
		with open(self.file_read, "r") as f_read, self.output().open("w") as f_out:
			count = sum(1 for _ in f_read)
			f_out.write(str(count-1))# 1 excludes header

class Extract_sample(luigi.Task):
	file_read=luigi.Parameter()
	perc=luigi.FloatParameter(default=0.01)

	def requires(self):
		return [Get_Var_numbers(file_read=self.file_read)]

	def output(self):
		return luigi.LocalTarget("{}/sample_{}.csv".format(folder, str(self.perc).replace(".", "-")))

	def run(self):
		limite_n=int(int(open("{}/count_{}".format(folder, self.file_read.replace(".csv", ".txt")), "r").read())*self.perc)

		with open(self.file_read) as f_read, self.output().open("w") as f_out:
			# Get headerline
			for line in f_read:
				f_out.write(line)
				break
			
			# If you want seed on random read
			# random.seed(34)
			# Get data
			for line in reservoir_sampling(f_read, limite_n):
				f_out.write(line)


class Import_mongo_from_file(luigi.Task):
	file_read=luigi.Parameter()
	perc=luigi.FloatParameter(default=0.01)

	# mongo parameters
	ip=luigi.Parameter(default="localhost")
	port=luigi.IntParameter(default=27017)

	db=luigi.Parameter(default="indiciados")
	collection=luigi.Parameter(default="sample")

	task_complete = False

	def requires(self):
		return [Extract_sample(file_read=self.file_read, perc=self.perc)]

	def run(self):
		if(self.collection=="sample"):
			collection_name="sample_{}".format(str(self.perc).replace(".", ""))
		else:
			collection_name=self.collection

		# Mongo data
		client=MongoClient(self.ip, self.port)
		db=client[self.db]
		collection=db[collection_name]

		# Clear collection before to import (prevent duplicated data)
		collection.drop()

		os.system("mongoimport --db '{}' --collection '{}' --type=csv --file '{}' --headerline".format(self.db, collection_name, "{}/sample_{}.csv".format(folder, str(self.perc).replace(".", "-"))))
		
		self.task_complete = True

	def complete(self):
		return  self.task_complete

class Filter_data(luigi.Task):
	file_read=luigi.Parameter()
	perc=luigi.FloatParameter(default=0.01)

	# mongo parameters
	ip=luigi.Parameter(default="localhost")
	port=luigi.IntParameter(default=27017)

	db=luigi.Parameter(default="indiciados")
	collection=luigi.Parameter(default="sample")

	# filter data
	filters=luigi.Parameter()
	output_file=luigi.Parameter(default="sample_filtered")

	task_complete = False

	def requires(self):
		return [Import_mongo_from_file(file_read=self.file_read, perc=self.perc, ip=self.ip, port=self.port, db=self.db, collection=self.collection)]


	def run(self):
		if(self.collection=="sample"):
			collection_name="sample_{}".format(str(self.perc).replace(".", ""))
		else:
			collection_name=self.collection

		if(self.output_file=="sample_filtered"):
			output="{}/sample_{}_filtered.csv".format(folder, str(self.perc).replace(".", "-"))
		else:
			output="{}/{}".format(folder, self.output_file)

		# Mongo data
		client=MongoClient(self.ip, self.port)
		db=client[self.db]
		collection=db[collection_name]

		# Like [{"$match":{"$and":[{"DEPARTAMENTO":"Risaralda"}, {"MUNICIPIO":"PEREIRA"}]}}]
		cursor=list(collection.aggregate(eval(self.filters)))

		df =  pd.DataFrame(cursor)

		# Delete the _id
		if '_id' in df:
			del df['_id']

		# export MongoDB documents to a CSV file
		df.to_csv(output, ",", index=False) # CSV delimited by commas

		self.task_complete = True
	
	def complete(self):
		return  self.task_complete

			
class Get_stadistics(luigi.Task): 
	file_read=luigi.Parameter()
	perc=luigi.FloatParameter(default=0.01)

	# mongo parameters
	ip=luigi.Parameter(default="localhost")
	port=luigi.IntParameter(default=27017)

	db=luigi.Parameter(default="indiciados")
	collection=luigi.Parameter(default="sample")

	# filter data
	filters=luigi.Parameter()
	output_file=luigi.Parameter(default="sample_filtered")

	# Analytics by...
	analytic=luigi.Parameter()
	stadistic_result_file=luigi.Parameter(default="stadistics_result")

	def requires(self):
		return [Filter_data(file_read=self.file_read, perc=self.perc, ip=self.ip, port=self.port, db=self.db, collection=self.collection, filters=self.filters, output_file=self.output_file)]
	
	def output(self):
		return luigi.LocalTarget("{}/{}.csv".format(folder,self.stadistic_result_file))
		
	def run(self):
		if(self.output_file=="sample_filtered"):
			filtered_file="{}/sample_{}_filtered.csv".format(folder, str(self.perc).replace(".", "-"))
		else:
			filtered_file=self.output_file

		df_filtered = pd.read_csv(filtered_file)

		df_filtered.groupby(self.analytic)["TOTAL_INDICIADOS"].mean()

		with self.output().open("w") as f_out:

			f_out.write("grouped,result,type_grouped")

			for enum, line_i in enumerate(str(df_filtered.groupby(self.analytic)["TOTAL_INDICIADOS"].mean()).split("\n")):
				if(enum==0):
					continue
				
				line_size=len(line_i.split("    "))
				if(line_size==1):
					break
				
				f_out.write("\n")
				for enum_line, line_j in enumerate(line_i.split("    ")):
					if(line_size-1==enum_line):
						f_out.write("{},mean".format(line_j.strip()))
					else:
						f_out.write("{},".format(line_j))

			for enum, line_i in enumerate(str(df_filtered.groupby(self.analytic)["TOTAL_INDICIADOS"].median()).split("\n")):
				if(enum==0):
					continue
				
				line_size=len(line_i.split("    "))
				if(line_size==1):
					break
				
				f_out.write("\n")
				for enum_line, line_j in enumerate(line_i.split("    ")):
					if(line_size-1==enum_line):
						f_out.write("{},median".format(line_j.strip()))
					else:
						f_out.write("{},".format(line_j))

			for enum, line_i in enumerate(str(df_filtered.groupby(self.analytic)["TOTAL_INDICIADOS"].std()).split("\n")):
				if(enum==0):
					continue
				
				line_size=len(line_i.split("    "))
				if(line_size==1):
					break
				
				f_out.write("\n")
				for enum_line, line_j in enumerate(line_i.split("    ")):
					if(line_size-1==enum_line):
						f_out.write("{},std".format(line_j.strip()))
					else:
						f_out.write("{},".format(line_j))


		data_dict={}

		for enum, line_i in enumerate(str(df_filtered.groupby(self.analytic)["TOTAL_INDICIADOS"].sum()).split("\n")):
			if(enum==0):
				continue
			
			line_size=len(line_i.split("    "))
			if(line_size==1):
				break
			
			if(line_size==2):
				key, data=line_i.split("    ")
				data=float(data.strip())

				data_dict[key]=data

		
		indices=np.arange(len(data_dict.values()))

		plot_title="Histogram"
		plt.close(plot_title)
		plt.figure(plot_title)

		plt.title(plot_title)

		rects=plt.bar(indices, data_dict.values())

		for rect, key in zip(rects, data_dict):
			plt.xlabel('var')
			plt.ylabel('quantity')

			height = rect.get_height()

			plt.annotate('{}\n{}'.format(key, data_dict.get(key)),
				xy=(rect.get_x() + rect.get_width() / 2, height),
				xytext=(0, 3),  # 3 points vertical offset
				textcoords="offset points",
				ha='center', va='bottom')

		file_path=os.path.join(folder, plot_title+".png")
		plt.savefig(file_path)
		plt.close(plot_title)

class Get_stadistics_and_sql(luigi.Task): 
	file_read=luigi.Parameter()
	perc=luigi.FloatParameter(default=0.01)

	# mongo parameters
	ip=luigi.Parameter(default="localhost")
	port=luigi.IntParameter(default=27017)

	db=luigi.Parameter(default="indiciados")
	collection=luigi.Parameter(default="sample")

	# filter data
	filters=luigi.Parameter()
	output_file=luigi.Parameter(default="sample_filtered")

	# Analytics by...
	analytic=luigi.Parameter()
	stadistic_result_file=luigi.Parameter(default="stadistics_result")

	# Sql script
	sql_name=luigi.Parameter(default="sql_script")
	sql_db_name=luigi.Parameter(default="mongo_results")

	mysql_user=luigi.Parameter(default="root")
	mysql_pass=luigi.Parameter(default="mongo477")


	def requires(self):
		return [Get_stadistics(file_read=self.file_read, perc=self.perc, ip=self.ip, port=self.port, db=self.db, collection=self.collection, filters=self.filters, output_file=self.output_file, analytic=self.analytic, stadistic_result_file=self.stadistic_result_file)]
	
	def output(self):
		return luigi.LocalTarget("{}/{}.sql".format(folder, self.sql_name))

	def run(self):
		with self.output().open("w") as f_out:
			# Add variable for import with local files
			f_out.write("SET GLOBAL local_infile=1;")
			# Create database on SQL
			f_out.write("CREATE DATABASE IF NOT EXISTS `{}` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;\n".format(self.sql_db_name))
			
			csv_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and ".csv" in f]			
			
			for file_i in csv_files:
				table_name=os.path.splitext(os.path.basename(file_i))[0]
				f_out.write("DROP TABLE IF EXISTS `{}`.`{}`;\n".format(self.sql_db_name, table_name))

			
				# making data frame  
				df = pd.read_csv(os.path.join(folder, file_i))
				
				f_out.write("CREATE TABLE `{}`.`{}` (\n".format(self.sql_db_name, table_name))

				# iterating the columns 
				for enum, col in enumerate(df.columns): 
					data_type=df.dtypes[col]

					# print("TYPE::", data_type)

					if("int" in str(data_type)):
						f_out.write("`{}` INT(10)".format(col))
					elif("float" in str(data_type)):
						f_out.write("`{}` FLOAT(10)".format(col))
					elif("bool" in str(data_type)):
						f_out.write("`{}` BOOL".format(col))
					elif("str" or "object" in str(data_type)):
						f_out.write("`{}` VARCHAR(255)".format(col))

					if(len(df.columns)-1 != enum):
						f_out.write(",\n")
					else:
						f_out.write("\n")

				f_out.write(");\n")

				f_out.write("LOAD DATA LOCAL INFILE '{}/{}' INTO TABLE `{}`.`{}` FIELDS TERMINATED BY '{}'  ENCLOSED BY '{}' IGNORE 1 LINES;\n".format(folder, file_i, self.sql_db_name, table_name, ",", '"'))#, str(["`"+str(i)+"`" for i in df.columns])[1:-1].replace("'", "")))
			
		os.system("mysql --local-infile=1 -u{} -p{} < {}".format(self.mysql_user, self.mysql_pass, "{}/{}.sql".format(folder, self.sql_name)))

				


				#LOAD DATA LOCAL INFILE 'students.csv' INTO TABLE students FIELDS TERMINATED BY ','  ENCLOSED BY '"' LINES TERMINATED BY 'n' (firstname,middlename,lastname,class,email)


if __name__ == "__main__":
	luigi.run()
