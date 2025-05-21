from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import datetime

COUCHDB_URL = 'http://localhost:5984'
DB_NAME = 'gymstorage'
COUCHDB_USER = 'admin'
COUCHDB_PASSWORD = 'admin'

def couchdb_headers():
    return {
        "Content-Type": "application/json"
    }

def couchdb_auth():
    return (COUCHDB_USER, COUCHDB_PASSWORD)

app = Flask(__name__)
CORS(app)  # Habilita CORS para integração com o front-end

@app.route('/itens', methods=['POST'])
def adicionar_item():
    data = request.json
    now = datetime.datetime.utcnow().isoformat()
    data['data_insercao'] = now
    data['data_atualizacao'] = now
    resp = requests.post(f"{COUCHDB_URL}/{DB_NAME}", json=data,
                         auth=couchdb_auth(), headers=couchdb_headers())
    return jsonify(resp.json()), resp.status_code

@app.route('/itens', methods=['GET'])
def listar_itens():
    query = {"selector": {}}
    # Filtros
    if 'categoria' in request.args:
        query['selector']['categoria'] = request.args['categoria']
    if 'status' in request.args:
        query['selector']['status'] = request.args['status']
    if 'nome' in request.args:
        query['selector']['nome'] = {"$regex": request.args['nome']}
    resp = requests.post(f"{COUCHDB_URL}/{DB_NAME}/_find", json=query,
                         auth=couchdb_auth(), headers=couchdb_headers())
    return jsonify(resp.json().get('docs', []))

@app.route('/itens/<id>', methods=['GET'])
def get_item_por_id(id):
    resp = requests.get(f"{COUCHDB_URL}/{DB_NAME}/{id}", auth=couchdb_auth())
    if resp.status_code == 200:
        return jsonify(resp.json())
    else:
        return jsonify({"erro": "Item não encontrado!"}), 404

@app.route('/itens/baixa-quantidade/<int:x>', methods=['GET'])
def baixa_quantidade(x):
    query = {"selector": {"quantidade": {"$lt": x}}}
    resp = requests.post(f"{COUCHDB_URL}/{DB_NAME}/_find", json=query,
                         auth=couchdb_auth(), headers=couchdb_headers())
    return jsonify(resp.json().get('docs', []))

@app.route('/itens/recentes', methods=['GET'])
def itens_recentes():
    query = {
        "selector": {},
        "sort": [{"data_insercao": "desc"}],
        "limit": 10  # Exemplo: últimos 10
    }
    resp = requests.post(f"{COUCHDB_URL}/{DB_NAME}/_find", json=query,
                         auth=couchdb_auth(), headers=couchdb_headers())
    return jsonify(resp.json().get('docs', []))

@app.route('/itens/atualizados', methods=['GET'])
def itens_atualizados():
    query = {
        "selector": {},
        "sort": [{"data_atualizacao": "desc"}],
        "limit": 10
    }
    resp = requests.post(f"{COUCHDB_URL}/{DB_NAME}/_find", json=query,
                         auth=couchdb_auth(), headers=couchdb_headers())
    return jsonify(resp.json().get('docs', []))

@app.route('/itens/<id>', methods=['PUT'])
def editar_item(id):
    data = request.json
    r = requests.get(f"{COUCHDB_URL}/{DB_NAME}/{id}", auth=couchdb_auth())
    if r.status_code != 200:
        return jsonify({"erro": "Item não encontrado!"}), 404
    data['_id'] = id
    data['_rev'] = data.get('_rev') or r.json()['_rev']
    resp = requests.put(f"{COUCHDB_URL}/{DB_NAME}/{id}", json=data, auth=couchdb_auth())
    return jsonify(resp.json()), resp.status_code

@app.route('/itens/<id>', methods=['DELETE'])
def deletar_item(id):
    rev = request.args.get('rev')
    if not rev:
        return jsonify({'erro': 'Rev obrigatória!'}), 400
    resp = requests.delete(f"{COUCHDB_URL}/{DB_NAME}/{id}?rev={rev}", auth=couchdb_auth())
    return jsonify(resp.json()), resp.status_code

if __name__ == '__main__':
    app.run(debug=True)