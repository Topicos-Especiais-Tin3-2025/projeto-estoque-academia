# Sistema de Controle de Estoque para Academia 🏋️‍♂️

Aplicação local construída com **Flask** e **CouchDB**, pensada para controle de equipamentos e acessórios de academias. Permite **inserir**, **editar**, **excluir** e **consultar** itens com filtros por data, status e categoria.

---
## ✅ Requisitos

- Python 3.10+
- CouchDB

## Tecnologias

- Backend: Python (Flask, Flask-CORS, Requests)
- Banco de Dados: CouchDB
- Frontend: HTML, CSS, JavaScript

---

## Instalação & Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/seuUsuario/seuRepositorio.git
cd seuRepositorio
```

### 2.  Instalar e Configurar o CouchDB
Instale o CouchDB.
Abra o painel web (Fauxton): http://localhost:5984/_utils/
Crie um banco chamado gymstorage.
Crie um usuário admin e senha se solicitado.
Anote usuário e senha para uso no backend.

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis do Backend
No arquivo app.py, ajuste os dados de conexão com o CouchDB conforme:

```bash
COUCHDB_URL = 'http://localhost:5984'
DB_NAME = 'gymstorage'
COUCHDB_USER = 'admin'      # Seu usuário
COUCHDB_PASSWORD = 'admin'  # Sua senha
```

### 5. Iniciar o Backend
```bash
python app.py
```
O backend rodará em http://127.0.0.1:5000
Teste com: http://127.0.0.1:5000/itens (deve ver um JSON)

### 6. Iniciar o Frontend
- Basta abrir o arquivo index.html (ou outros HTMLs do projeto) no navegador.
- Recomendado: Chrome, Firefox ou Edge.

### 7. Usando o Sistema
- Cadastro: clique em "Adicionar Item" no topo do index.
- Edição: clique no ícone de editar na tabela principal e modifique os dados.
- Exclusão: na tela de edição, use o botão "Excluir".
- Filtros: utilize as caixas de filtro para buscar itens por nome,  categoria, -status ou valor.
- Histórico: veja as movimentações completas na tela "Histórico".

### 8. Observações Finais
O sistema é totalmente responsivo e funciona apenas abrindo os arquivos HTML.
CouchDB deve estar sempre rodando em segundo plano.
Não esqueça de manter o app.py (backend) ativo para conexão entre frontend e banco.