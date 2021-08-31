# flask

```python
import flask

app=flask.Flask(__name__)


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



if __name__ == "__main__":
        app.run(debug=True, port=40500, host="0.0.0.0")
```




