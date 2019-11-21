from flask import Flask
from flask_restful import Api
from APS1 import Lista_Tarefas, Tarefas

app = Flask(__name__)
api = Api(app)

api.add_resource(Lista_Tarefas, '/Tarefa')
api.add_resource(Tarefas, '/Tarefa/<id_tarefa>')

@app.route('/healthcheck')
def Healthcheck():
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)