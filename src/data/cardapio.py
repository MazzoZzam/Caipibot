from sqlalchemy import Table, Column, Integer, String, DECIMAL, func, select
from ..database.conexao import meta, conn

# mapeando tabela cardapio
cardapio = Table (
    "cardapio",
    meta,
    Column('id_item', Integer, primary_key = True),
    Column('nome_item', String(50), nullable = False),
    Column('preco', DECIMAL(6, 2), nullable = False)
)

def verificar_cardapio():
    select_itens = select(func.count()).select_from(cardapio)

    result = conn.execute(select_itens).fetchone()

    return result[0]

def criar_cardapio():
    create_cardapio = cardapio.insert().values([
		{'nome_item': 'ovos de codorna com salame', 'preco': 49.00},
		{'nome_item': 'pao de alho caseiro ', 'preco': 48.00},
		{'nome_item': 'batata chips', 'preco': 23.50},
		{'nome_item': 'bolinho de arroz', 'preco': 29.99},
		{'nome_item': 'sacanagem com mortadela e cenoura', 'preco': 14.99},
		{'nome_item': 'batatas assadas', 'preco': 30.00},
		{'nome_item': 'amendoim picante', 'preco': 15.00},
		{'nome_item': 'onion rings', 'preco': 39.90},
		{'nome_item': 'linguica com cebola', 'preco': 19.90},
		{'nome_item': 'itaipava garrafa', 'preco': 4.50},
		{'nome_item': 'skol garrafa', 'preco': 4.50},
		{'nome_item': 'heineken garrafa', 'preco': 8.99},
		{'nome_item': 'brahma garrafa', 'preco': 5.99},
		{'nome_item': 'antarctica garrafa', 'preco': 4.99},
		{'nome_item': 'corona garrafa', 'preco': 7.99},
		{'nome_item': 'whisky black label johnnie walker', 'preco': 122.00},
		{'nome_item': 'whisky chivas regal', 'preco': 119.90},
		{'nome_item': 'licor jagermeister', 'preco': 115.00},
		{'nome_item': 'absolut vodka', 'preco': 74.99},
		{'nome_item': 'vinho concha y toro reservado', 'preco': 29.99},
		{'nome_item': 'whisky jack daniels', 'preco': 199.90},
		{'nome_item': 'vodka smirnoff', 'preco': 74.99},
		{'nome_item': 'whisky ballantines american barrel', 'preco': 79.99},
		{'nome_item': 'rum bacardi carta blanca', 'preco': 49.99},
		{'nome_item': 'martini vermute rosso', 'preco': 44.99},
		{'nome_item': 'sucos', 'preco': 18.00},
		{'nome_item': 'guarana antarctica lata', 'preco': 6.99},
		{'nome_item': 'coca cola lata', 'preco': 6.99},
		{'nome_item': 'H2O limao', 'preco': 7.99},
		{'nome_item': 'agua sem gas', 'preco': 3.99}
	])
    conn.execute(create_cardapio)
    conn.commit()
    


# exibindo cardapio
def mostrar_cardapio():
    select_foods = cardapio.select().where(cardapio.c.id_item <= 9)
    select_beers = cardapio.select().where(cardapio.c.id_item >= 10, cardapio.c.id_item < 26)
    select_drinks = cardapio.select().where(cardapio.c.id_item > 25)

    result_food = conn.execute(select_foods)
    result_beer = conn.execute(select_beers)
    result_drink = conn.execute(select_drinks)
    
    pestico = ""
    bebida = ""
    drink = ""
    
    for item in result_food.fetchall():
        pestico += f"{item[0]}. {item[1]} - R${item[2]} \n"
    
    
    for item in result_beer.fetchall():
        bebida += f"{item[0]}. {item[1]} - R${item[2]} \n"
    
    
    for item in result_drink.fetchall():
        drink += f"{item[0]}. {item[1]} - R${item[2]} \n"
        
    return ("PETISCOS: \n"
    		f"{pestico}\n"
            "BEBIDAS ALCOOLICAS: \n"
            f"{bebida}\n"
            "BEBIDAS NAO-ALCOOLICAS: \n"
            f"{drink}")
