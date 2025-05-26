from sqlalchemy import MetaData, Table, Column, Integer, String, select
from ..database.conexao import engine

conn = engine.connect()

# construindo tabela
meta = MetaData()

# mapeando tabela cliente
cliente = Table (
    "cliente",
    meta,
    Column('id_cliente', Integer, primary_key = True),
    Column('nome_cliente', String, nullable = False),
    Column('telefone', String, nullable = False),
    Column('endereco', String, nullable = False)
)

# inserindo cliente
def inserir_cliente(nome, tel, end):
    try:
        insert_client = cliente.insert().values(nome_cliente = nome, telefone = tel, endereco = end)
        conn.execute(insert_client)
        conn.commit()

        print(f"Cliente - {nome} registrado com sucesso!")

        conn.close()
    except Exception as e:
        print(f"Nao foi possivel registrar cliente, tente mais tarde: {e}")
    

# obter id do cliente
def obter_id():
    select_client = select(cliente.c.id_cliente)
    result = conn.execute(select_client).fetchone()

    return result[0]

def main():
    obter_id()

if __name__ == "__main__":
    main()
