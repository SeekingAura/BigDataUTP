import flask
from flask_pymongo import PyMongo
# import mongo

app=flask.Flask(__name__)
app.config['MONGO_DBNAME']="vehiculos"
app.config["MONGO_URI"]="mongodb://27017/vehiculos"

mongo = PyMongo(app)

@app.route("/", methods=["GET"])
def inicio():
	return "<h1>Conexión a servicio</h1>"

datos= [{"id":1, "nombre":"Juan Perez"}, {"id":2, "nombre":"Ana Lopez"}, {"id":3, "nombre":"Mario Gomez"}]

@app.route("/datos", methods=["GET"])
def api_datos():
	return flask.jsonify(datos)

#ip:40500/usuario?id=2
@app.route("/usuario", methods=["GET"])
def api_usr():
	if("id" in flask.request.args):
		id=flask.request.args["id"]
	else:
		return "parametro no encontrado"

	respuesta=[]

	for d in datos:
		if str(d["id"])==id:
			respuesta.append(d)

	if len(respuesta)>0:
		return flask.jsonify(respuesta)
	else:
		return "id no encontrado"

@app.route("/mazdas", methods=["GET"])
def vehiculos_mongo():
	ls=mongo.db.automotor.find_one()
	#print(ls)
	#result=[]
	#for key in ls:
	#	result.append(ls.get(key))
	# result=[ls.get(key) for key in ls]
	res={"PLACA":ls["PLACA"], "modelo":ls["MODELO"]}
	#print(result)
	return flask.jsonify(res)
	


if __name__ == "__main__":
	app.run(debug=True, port=40500, host="0.0.0.0")
