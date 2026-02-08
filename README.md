# 🚀 Meu Primeiro Projeto API - FastAPI & Postgres

Este é o meu primeiro projeto desenvolvendo uma API robusta, integrando Python com banco de dados relacional e containers Docker.

## 🛠️ Tecnologias Utilizadas
* **FastAPI**: Framework moderno e de alta performance para Python.
* **PostgreSQL**: Banco de dados relacional para persistência dos dados.
* **Docker**: Containerização do ambiente de banco de dados.
* **SQLAlchemy**: ORM para comunicação eficiente com o banco.
* **Pydantic**: Validação de dados e segurança nas rotas.

## ⚙️ Como rodar o projeto
1. Clone o repositório.
2. Crie seu ambiente virtual: `python -m venv .venv` e ative-o.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Suba o banco de dados com Docker: 
   `docker run --name postgres-db -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres`
5. Configure seu arquivo `.env` com a URL do banco.
6. Rode as migrações: `python criar_banco.py`.
7. Inicie o servidor: `uvicorn main:app --reload`.

## 📌 Rotas Disponíveis
* `GET /usuarios`: Lista todos os usuários cadastrados.
* `POST /usuarios`: Cadastra um novo usuário (JSON: `{"nome": "Seu Nome"}`).
