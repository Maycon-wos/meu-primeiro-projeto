from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(os.getenv("DATABASE_URL"))


# Modelo de dados (O Segurança da Portaria)
class Usuario(BaseModel):
    nome: str


@app.get("/usuarios")
def listar_usuarios():
    with engine.connect() as conexao:
        resultado = conexao.execute(text("SELECT * FROM usuarios"))
        # Converte as linhas do banco em uma lista de dicionários
        return [dict(linha._mapping) for linha in resultado]


@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    with engine.connect() as conexao:
        conexao.execute(
            text("INSERT INTO usuarios (nome) VALUES (:nome)"), {"nome": usuario.nome}
        )
        conexao.commit()
    return {"status": "Sucesso", "usuario_criado": usuario.nome}
