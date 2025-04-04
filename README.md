# Sistema de Controle de Estoque para Academia 🏋️‍♂️

Aplicação local construída com **Flask** e **CouchDB**, pensada para controle de equipamentos e acessórios de academias. Permite **inserir**, **editar**, **excluir** e **consultar** itens com filtros por data, status e categoria.

---

## ✅ Requisitos

- Python 3.10+
- Docker Desktop (para rodar o banco CouchDB)

---

## 📁 Estrutura do Projeto

```
estoque_academia/
├── app.py
├── db.py
├── requirements.txt
├── docker-compose.yml
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── add_item.html
    └── update_item.html
```

---

## ⚙️ Setup Rápido

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/estoque_academia.git
cd estoque_academia
```

### 2. Suba o CouchDB com Docker
```bash
docker-compose up -d
```

Acesse no navegador: http://localhost:5984/_utils/  
Login: `admin` — Senha: `admin`

Crie um banco chamado:
```
estoque
```

### 3. Prepare o ambiente Python

#### (opcional, mas recomendado)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/macOS
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Rode o servidor Flask
```bash
python app.py
```

### 6. Acesse no navegador
```
http://127.0.0.1:5000
```

---

## 🧠 Funcionalidades
- Inserção de itens com nome, categoria, quantidade e status
- Atualização de status e quantidade
- Exclusão de itens
- Listagem de itens em tabela com filtros planejados

---

## 👥 Equipe
Este projeto está sendo desenvolvido por Gustavo e seu time na disciplina de Tópicos Especiais em Engenharia da Computação na Facens.

---

## 📌 Licença
Projeto educacional — uso livre com créditos à equipe.
