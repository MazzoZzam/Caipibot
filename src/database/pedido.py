from collections import defaultdict
from sqlalchemy import Table, Column, Integer, DateTime, ForeignKey, select, Enum, func
from ..database.conexao import meta, conn
from ..database.cliente import cliente
from ..data.cardapio import cardapio
from ..algorithms.linked_list import LinkedList

lista = LinkedList()

# mapeando tabela pedido
pedido = Table (
    "pedido", 
    meta,
    Column('id_pedido', Integer, primary_key=True),
    Column('data_pedido', DateTime, nullable=False, server_default=func.now()),
    Column('id_cliente', Integer, ForeignKey(cliente.c.id_cliente), nullable=False),
    Column('estado_pedido', Enum("em processo", "aprovado"), nullable=False, server_default="em processo")
)

# mapeando tabela item_pedido
item_pedido = Table (
    "item_pedido",
    meta,
    Column('id_item_pedido', Integer, primary_key=True),
    Column('id_item', Integer, ForeignKey(cardapio.c.id_item), nullable=False),
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

    # selecionando dados na lista
    client_select = select(cliente.c.nome_cliente, 
                           cliente.c.telefone,
                           cliente.c.endereco).where(cliente.c.id_cliente == pedido.c.id_cliente)

    data_select = select(pedido.c.data_pedido).where(pedido.c.id_pedido == id_new_order)

    price_select = select(func.sum(cardapio.c.preco)).where(cardapio.c.id_item.in_(lista_itens))

    client_result = conn.execute(client_select).fetchone()
    data_result = conn.execute(data_select).fetchone()
    price_result = conn.execute(price_select).fetchone()

    lista.novo_pedido(id_new_order, 
                      client_result[0],
                      client_result[1],
                      client_result[2],
                      data_result[0],
                      lista_itens,
                      price_result[0])
    
def inserir_pedido_lista():
    itens_list = defaultdict(lambda:{
        "itens": [],
        "total": 0
    })

    orders_select = select(pedido.c.id_pedido, 
                           cliente.c.nome_cliente, 
                           cliente.c.telefone, 
                           cliente.c.endereco,
                           pedido.c.data_pedido
                           ).select_from(pedido.join(cliente)).where(pedido.c.estado_pedido == "em processo")
    
    itens_select = select(item_pedido.c.id_pedido, cardapio.c.nome_item, cardapio.c.preco).join(cardapio)
    
    orders_result = conn.execute(orders_select).fetchall()
    itens_result = conn.execute(itens_select).fetchall()

    for id_pedido, item, preco in itens_result:
        itens_list[id_pedido]["itens"].append(item)
        itens_list[id_pedido]["total"] += float(preco)

    for order in orders_result:
        itens = itens_list[order[0]]["itens"]
        total = itens_list[order[0]]["total"]

        lista.novo_pedido(order[0], order[1], order[2], order[3], order[4], itens, total)

def atualizar_pedido(id_pedido):
    status_update = pedido.update().where(pedido.c.id_pedido == id_pedido).values(estado_pedido = "aprovado")

    conn.execute(status_update)

    conn.commit()

def ver_aprovados():
    select_orders = select(pedido.c.id_pedido,
                           cliente.c.nome_cliente, 
                           cliente.c.telefone, 
                           cliente.c.endereco,  
                           pedido.c.data_pedido, 
                           cardapio.c.nome_item, 
                           cardapio.c.preco).select_from(
                            pedido.join(cliente).join(item_pedido).join(cardapio)).where(
                            pedido.c.estado_pedido == "aprovado")
    
    result_order = conn.execute(select_orders).fetchall()

    approved = ""

    for item in result_order:
        approved += f"""
        ID do pedido - {item[0]}, \n
        Nome Cliente - {item[1]}, \n
        Telefone - {item[2]}, \n
        Endereço - {item[3]}, \n
        Data do Pedido - {item[4]}, \n
        Itens - {item[5]}, \n
        Valor do Pedido - {item[6]} \n
        *--------------------------*
        """

    return approved

