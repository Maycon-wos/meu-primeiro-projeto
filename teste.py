from sqlalchemy import create_engine, text

# Conectando no banco que você viu no DBeaver
URL_BANCO = "postgresql://postgres:estudante@localhost:5432/postgres"
engine = create_engine(URL_BANCO)

def testar_tudo():
    try:
        with engine.connect() as conexao:
            # 1. Inserir um dado
            conexao.execute(text("INSERT INTO usuarios (nome) VALUES ('MKN Dev')"))
            conexao.commit() # Salva no banco
            print("✅ Usuário inserido com sucesso!")

            # 2. Ler os dados
            resultado = conexao.execute(text("SELECT * FROM usuarios"))
            for linha in resultado:
                print(f"👤 Usuário no banco: {linha.nome}")
                
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    testar_tudo()