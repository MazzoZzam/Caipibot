from sqlalchemy import MetaData, Table, Column, Integer, DateTime, ForeignKey, select, func
from ..database.conexao import engine
from ..database.cliente import cliente
from ..data.cardapio import cardapio

conn = engine.connect()

# construindo estrutura tabela
meta = MetaData()

# mapeando tabela pedido
pedido = Table (
    "pedido", 
    meta,
    Column('id_pedido', Integer, primary_key=True),
    Column('data_pedido', DateTime, nullable=False, server_default = func.now()),
    Column('id_cliente', Integer, ForeignKey(cliente.c.id_cliente), nullable=False)
)

# mapeando tabela item_pedido
item_pedido = Table (
    "item_pedido",
    meta,
    Column('id_item_pedido', Integer, primary_key=True),
    Column('id_item', Integer, ForeignKey(cardapio.c.id_item), nullable=False),
    Column('id_pedido', Integer, ForeignKey('pedido.id_pedido'), nullable=False)
)

try:
    meta.create_all(engine)
except Exception as e:
    print(f"Deu nao: {e}")

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

def ver_pedido(cliente_id):
    # contruindo SELECT
    select_orders = select(cliente.c.nome_cliente, 
                           cliente.c.telefone, 
                           cliente.c.endereco, 
                           pedido.c.id_pedido, 
                           pedido.c.data_pedido, 
                           cardapio.c.nome_item, 
                           cardapio.c.preco).select_from(
                            pedido.join(cliente).join(item_pedido).join(cardapio)).where(
                            cliente.c.id_cliente == cliente_id)

    result = conn.execute(select_orders)

    # exibindo pedido
    for item in result.fetchall():
        print(item)

    # fechando conexao
    conn.close()




