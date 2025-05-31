from sqlalchemy import Table, Column, Integer, String, select
from ..database.conexao import meta, conn

# mapeando tabela cliente
cliente = Table (
    "cliente",
    meta,
    Column('id_cliente', Integer, primary_key = True),
    Column('nome_cliente', String(30), nullable = False),
    Column('telefone', String(15), nullable = False),
    Column('endereco', String(100), nullable = False)
)

# inserindo cliente
def inserir_cliente(nome, tel, end):
    try:
        insert_client = cliente.insert().values(nome_cliente = nome, telefone = tel, endereco = end)
        conn.execute(insert_client)
        conn.commit()

        print(f"Cliente - {nome} registrado com sucesso!")

    except Exception as e:
        print(f"Nao foi possivel registrar cliente, tente mais tarde: {e}")
    

# obter id do cliente
def obter_id(nome, tel, end):
    select_id_client = select(cliente.c.id_cliente).where(cliente.c.nome_cliente == nome, cliente.c.telefone == tel, cliente.c.endereco == end)
    result = conn.execute(select_id_client).fetchone()

    return result[0]