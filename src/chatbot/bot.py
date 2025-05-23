from chatbot.mensagens import MENSAGENS
from data.cardapio import CARDAPIO
from utils.calculos import calcular_tempo_entrega

# dicionario do estado e dados da conversa
estado_conversa = {
    "etapa": "nome",
    "nome": "",
    "telefone": "",
    "endereco": "",
    "pedido": [],
}

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
            tempo_preparo, tempo_entrega = calcular_tempo_entrega(total)
            
            # Exibindo "extrato" do usuario
            return (
                f"Pedido finalizado!\n"
                f"Nome: {estado_conversa['nome']}\n"
                f"Telefone: {estado_conversa['telefone']}\n"
                f"Endereço: {estado_conversa['endereco']}\n"
                f"Total: R$ {total:.2f}\n"
                f"Tempo de preparo: {tempo_preparo} min\n"
                f"Tempo de entrega: {tempo_entrega} min\n"
                "Obrigado pelo seu pedido!"
            )
        else: # caso não encontrar item no cardapio
            return "Item não encontrado. Digite o nome exato do produto como no cardápio ou 'finalizar'."

def mostrar_cardapio():
    mensagem = "CARDÁPIO:\n"
    # Exibindo cada item do cardapio
    for item in CARDAPIO:
        mensagem += f"- {item['nome']} - R$ {item['preco']:.2f}\n"
    mensagem += "\nDigite o nome do item que deseja ou 'finalizar'."
    return mensagem
