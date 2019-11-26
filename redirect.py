import requests, os, json
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

username = 'GiuPassarelli'
senha = 'banana'
ip = os.environ['IPDB']
porta = '5000'

requests.put('http://%s:%s@%s:%s/albums' % (username, senha, ip, porta))
res = requests.get('http://%s:%s/_uuids' % (ip, porta))
uuid = res.json()['uuids'][0]
dados_a_serem_salvos = '{"Nome":"Carlos","Instrumento":"Guitarra"}'

res = requests.put('http://%s:%s@%s:%s/albums/%s' % (username, senha, ip, porta, uuid), data=dados_a_serem_salvos)

dados_a_serem_salvos = ['{"Nome":"Pedro","Instrumento":"Guitarra"}','{"Nome":"Magda","Instrumento":"Piano"}','{"Nome":"Jubileu","Instrumento":"Saxofone"}']

for i in dados_a_serem_salvos:
    
    res = requests.get('http://%s:%s/_uuids' % (ip, porta))
    # Salvando o ID gerado
    uuid = res.json()['uuids'][0]
    # Salvando dados
    res = requests.put('http://%s:%s@%s:%s/albums/%s' % (username,senha,ip,porta,uuid),data=i)

@app.route('/healthcheck')
def Healthcheck():
    return '', 200

@app.route('/Tarefa', methods=['GET'])
def get_tarefa():
    res = requests.get('http://%s:%s/albums/_all_docs' % (ip,porta))
    res = res.json()
    ids = []
    new_json = {}
    for i in res:
        ids.append(i["id"])
        res2 = requests.get('http://%s:%s/albums/_all_docs/%s' % (ip,porta,i["id"]))
        temp_dict = res2.json()
        del temp_dict["_id"]
        del temp_dict["_rev"]
        new_json[i["id"]] = temp_dict
    print(new_json)

    return new_json, 200

# @app.route('/Tarefa', methods=['POST'])
# def post_tarefa():


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=False)