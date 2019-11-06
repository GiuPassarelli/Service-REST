from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

dict_tarefas = {
    1: {'tarefa': 'tarefa1'},
    2: {'tarefa': 'tarefa2'},
    3: {'tarefa': 'tarefa3'},
}

parser = reqparse.RequestParser()
parser.add_argument('tarefa')

class Lista_Tarefas(Resource):
    def get(self):
        return dict_tarefas

    def post(self):
        args = parser.parse_args()
        id_tarefa = max(dict_tarefas.keys()) + 1
        dict_tarefas[id_tarefa] = {'tarefa': args['tarefa']}
        return dict_tarefas[id_tarefa], 201

class Tarefas(Resource):
    def get(self, id_tarefa):
        return dict_tarefas[int(id_tarefa)]

    def put(self, id_tarefa):
        args = parser.parse_args()
        tarefa = {'tarefa': args['tarefa']}
        dict_tarefas[int(id_tarefa)] = tarefa
        return tarefa, 201

    def delete(self, id_tarefa):
        del dict_tarefas[4]
        return '', 204

class Healthcheck(Resource):
    def get(self):
    	return '', 200

api.add_resource(Lista_Tarefas, '/Tarefa')
api.add_resource(Tarefas, '/Tarefa/<id_tarefa>')
api.add_resource(Healthcheck, '/healthcheck')

if __name__ == '__main__':
    app.run(debug=True)