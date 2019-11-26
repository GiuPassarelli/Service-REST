import requests, os, json

username = 'GiuPassarelli'
senha = 'banana'
ip = os.environ['IPDB']
porta = '5000'

requests.put('http://%s:%s@%s:%s/albums' % (username, senha, ip, porta))
res = requests.get('http://%s:%s/_uuids' % (ip, porta))
uuid = res.json()['uuids'][0]
dados_a_serem_salvos = '{"Nome":"Carlos","Instrumento":"Guitarra"}'

res = requests.put('http://%s:%s@%s:%s/albums/%s' % (username, senha, ip, porta, uuid), data=dados_a_serem_salvos)
