from sqlalchemy import MetaData, Table, Column, Integer, DateTime, ForeignKey, func, text
from ..database.conexao import engine

conn = engine.connect()

# construindo estrutura tabela
meta = MetaData()

# mapeando tabela pedido
pedido = Table (
    "pedido", 
    meta,
    Column('id_pedido', Integer, primary_key=True),
    Column('data_pedido', DateTime, nullable=False, server_default = func.now()),
    Column('id_cliente', Integer, ForeignKey('cliente.id_cliente'), nullable=False)
)

# mapeando tabela item_pedido
item_pedido = Table (
    "item_pedido",
    meta,
    Column('id_item_pedido', Integer, primary_key=True),
    Column('id_item', Integer, ForeignKey('cardapio.id_item'), nullable=False),
    Column('id_pedido', Integer, ForeignKey('pedido.id_pedido'), nullable=False)
)

# inserir novo pedido
def inserir_pedido(id_cliente, lista_itens):
    # inserindo novo pedido, associando com cliente
    new_order = pedido.insert().values(id_cliente = id_cliente)
    result = conn.execute(new_order)

    # retirando id de id_pedido da tabela pedido
    id_new_order = result.inserted_primary_key[0]
    print(f"Pedido - {id_new_order} feito com sucesso!")

    # inserindo itens relacionados obtidos
    for id_item in lista_itens:
        conn.execute(item_pedido.insert().values(id_item = id_item, id_pedido = id_new_order))

    # enviando pedidos ao banco de dados
    conn.commit()

    # fechando conexao
    conn.close()

def ver_pedido():
    # contruindo SELECT
    query = """SELECT 
    cliente.nome_cliente,
    cliente.telefone,
    cliente.endereco,
    pedido.id_pedido,
    pedido.data_pedido,
    cardapio.nome_item,
    cardapio.preco
    FROM pedido
    JOIN cliente ON cliente.id_cliente = pedido.id_cliente
    JOIN item_pedido ON item_pedido.id_pedido = pedido.id_pedido
    JOIN cardapio ON cardapio.id_item = item_pedido.id_item"""
    

    result = conn.execute(text(query))

    # exibindo pedido
    for item in result.fetchall():
        print(item)

    # fechando conexao
    conn.close()

