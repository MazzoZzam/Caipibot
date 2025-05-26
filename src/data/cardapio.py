from sqlalchemy import MetaData, Table, Column, Integer, String, DECIMAL
from ..database.conexao import engine

conn = engine.connect()

# construindo tabela
meta = MetaData()

# mapeando tabela cardapio
cardapio = Table (
    "cardapio",
    meta,
    Column('id_item', Integer, primary_key = True),
    Column('nome_item', String, nullable = False),
    Column('preco', DECIMAL(6, 2), nullable = False)
)

# exibindo cardapio
def mostrar_cardapio():
    select_itens = cardapio.select()

    result = conn.execute(select_itens)

    for item in result.fetchall():
        print(item)

    conn.close()
