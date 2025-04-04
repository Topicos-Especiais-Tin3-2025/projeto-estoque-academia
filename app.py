from flask import Flask, render_template, request, redirect, url_for
import requests
import datetime

app = Flask(__name__)

COUCHDB_URL = "http://localhost:5984"
DB_NAME = "estoque"
auth = ('admin', 'admin')  # autenticação CouchDB

# Função para criar banco se não existir
def criar_banco():
    r = requests.put(f"{COUCHDB_URL}/{DB_NAME}", auth=auth)
    return r.status_code in [200, 201, 412]  # 412 = já existe

criar_banco()

@app.route('/')
def index():
    query = {
        "selector": {},
        "sort": [{"data_insercao": "desc"}]
    }
    r = requests.post(f"{COUCHDB_URL}/{DB_NAME}/_find", json=query, auth=auth)
    itens = r.json().get("docs", [])
    return render_template("index.html", itens=itens)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        novo_item = {
            "nome": request.form['nome'],
            "categoria": request.form['categoria'],
            "quantidade": int(request.form['quantidade']),
            "status": request.form['status'],
            "data_insercao": datetime.datetime.now().isoformat(),
            "data_atualizacao": datetime.datetime.now().isoformat()
        }
        requests.post(f"{COUCHDB_URL}/{DB_NAME}", json=novo_item, auth=auth)
        return redirect(url_for('index'))
    return render_template("add_item.html")

@app.route('/update/<id>', methods=['GET', 'POST'])
def update_item(id):
    r = requests.get(f"{COUCHDB_URL}/{DB_NAME}/{id}", auth=auth)
    item = r.json()
    if request.method == 'POST':
        item['quantidade'] = int(request.form['quantidade'])
        item['status'] = request.form['status']
        item['data_atualizacao'] = datetime.datetime.now().isoformat()
        requests.put(f"{COUCHDB_URL}/{DB_NAME}/{id}", json=item, auth=auth)
        return redirect(url_for('index'))
    return render_template("update_item.html", item=item)

@app.route('/delete/<id>/<rev>')
def delete_item(id, rev):
    requests.delete(f"{COUCHDB_URL}/{DB_NAME}/{id}?rev={rev}", auth=auth)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)