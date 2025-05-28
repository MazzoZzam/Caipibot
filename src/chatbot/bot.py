from ..chatbot.mensagens import MENSAGENS
from ..database.cliente import inserir_cliente, obter_id
from ..data.cardapio import mostrar_cardapio
from ..database.pedido import inserir_pedido

conversa = {
    "etapa": "nome",
    "nome_cliente": "",
    "telefone_cliente": "",
    "endereco": ""
}

def perguntar_nome(mensagem):
    estado_conversa["nome"] = mensagem
    estado_conversa["etapa"] = "telefone"
    return MENSAGENS["telefone"]

def perguntar_telefone(mensagem):
    estado_conversa["telefone"] = mensagem
    estado_conversa["etapa"] = "endereco"
    return MENSAGENS["endereco"]

def perguntar_endereco(mensagem):
    estado_conversa["endereco"] = mensagem
    estado_conversa["etapa"] = "menu"

    # inserindo informacoes do cliente no banco
    nome = estado_conversa.get("nome")
    telefone = estado_conversa.get("telefone")
    endereco = estado_conversa.get("endereco")

    inserir_cliente(nome, telefone, endereco)

    return apresentar_menu()

def apresentar_menu(mensagem):
    etapa = estado_conversa["etapa"]
    print("Escolha uma opção:", ["1️⃣ Fazer pedido", "2️⃣ Ver pedidos", "3️⃣ Gerenciar pedidos", "4️⃣ Realizar pedidos"])

    op = mensagem.strip().lower

    if op == "1" or op == "fazer pedido":
        estado_conversa["etapa"] = "fazer_pedido"   	 
        return fazer_pedido()
    
    elif op == "2" or op == "ver pedido":
        return "Vendo pedido"
    
    elif op == "3" or op == "gerenciar pedido":
        return "Gerenciando pedido"
    
    elif op == "4" or op == "realizar pedido":
        return "Realizando pedido"
    
    else:
        "Esta etapa nao existe, tente novamente por favor"

'''
def processar_mensagem(mensagem):
    etapa = estado_conversa["etapa"]

    # Perguntar nome do usuário
    if etapa == "nome":
        estado_conversa["nome"] = mensagem
        estado_conversa["etapa"] = "telefone"
        return MENSAGENS["telefone"]

    # Perguntar telefone do usuário
    elif etapa == "telefone":
        estado_conversa["telefone"] = mensagem
        estado_conversa["etapa"] = "endereco"
        return MENSAGENS["endereco"]

    # Perguntar endereço do usuário
    elif etapa == "endereco":
        estado_conversa["endereco"] = mensagem
        estado_conversa["etapa"] = "menu"
        return mostrar_cardapio()

    # Mostrar e fazer pedido
    elif etapa == "menu":
        # Limpeza de input, sem espaços e letras minusculas
        item_escolhido = mensagem.strip().lower()
        
        # Tentando encontrar itens no cardapio de acordo com o input do usuario 
        item_encontrado = next((item for item in CARDAPIO if item['nome'].lower() == item_escolhido), None)

        if item_encontrado: # item encontrado
            estado_conversa["pedido"].append(item_encontrado)
            return f"Item '{item_encontrado['nome']}' adicionado. Deseja mais alguma coisa? Se não, digite 'finalizar'."
        elif mensagem.lower() == "finalizar": # pedido finalizado
            # calcular preço total dos itens pedidos
            total = sum(item['preco'] for item in estado_conversa["pedido"])
            
            # calcular tempo de preparo e entrega
           
            
            # Exibindo "extrato" do usuario
            return (
                f"Pedido finalizado!\n"
                f"Nome: {estado_conversa['nome']}\n"
                f"Telefone: {estado_conversa['telefone']}\n"
                f"Endereço: {estado_conversa['endereco']}\n"
                f"Total: R$ {total:.2f}\n"
                "Obrigado pelo seu pedido!"
            )
        else: # caso não encontrar item no cardapio
            return "Item não encontrado. Digite o nome exato do produto como no cardápio ou 'finalizar'."
'''


def fazer_pedido():
    pedidos = []

    id_cliente = obter_id()

    mostrar_cardapio()
    print("Insira o numero do pedido, digite 'finalizar' quando terminar")

    inserir_pedido(id_cliente, pedidos)

    

    

# dicionario do estado e dados da conversa
estado_conversa = {
    "nome": perguntar_nome,
    "telefone": perguntar_telefone,
    "endereco": perguntar_endereco,
    "menu": apresentar_menu,
    "fazer_pedido": fazer_pedido,
    # "ver_pedido": ver_pedido,
    # "gerenciar_pedido": gerenciar_pedido,
    # "realizar_pedido": realizar_pedido  
}

def main(): 
    print("a")

if __name__ == "__main__":
    main()
