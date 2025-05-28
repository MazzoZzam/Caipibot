from sqlalchemy import create_engine

# criando conexao com o banco de dados
engine = create_engine(
    "mysql+pymysql://root@localhost:3306/caipibot_database?charset=utf8mb4",
    echo = True
)

# testando conexao
try:
    conn = engine.connect()
    print("Banco de dados conectado com sucesso")
except Exception as e:
    print(f"Conexao falhou: {e}")