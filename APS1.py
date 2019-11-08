from flask import Flask
from flask_restful import Resource, Api, reqparse

dict_tarefas = {}

id_count = 0

parser = reqparse.RequestParser()
parser.add_argument('titulo', location='json')
parser.add_argument('texto', location='json')

class Lista_Tarefas(Resource):
    def get(self):
        return dict_tarefas

    def post(self):
        args = parser.parse_args()
        global id_count
        id_count += 1
        dict_tarefas[id_count] = {'titulo': args['titulo'], 'texto': args['texto']}
        return dict_tarefas[id_count], 201

class Tarefas(Resource):
    def get(self, id_tarefa):
        return dict_tarefas[int(id_tarefa)]

    def put(self, id_tarefa):
        args = parser.parse_args()
        tarefa = {'titulo': args['titulo'], 'texto': args['texto']}
        dict_tarefas[int(id_tarefa)] = tarefa
        return tarefa, 201

    def delete(self, id_tarefa):
        del dict_tarefas[int(id_tarefa)]
        return '', 204