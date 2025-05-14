from chatbot.mensagens import MENSAGENS
from data.cardapio import CARDAPIO
from utils.calculos import calcular_tempo_entrega

estado_conversa = {
    "etapa": "nome",
    "nome": "",
    "telefone": "",
    "endereco": "",
    "pedido": [],
}

def processar_mensagem(mensagem):
    etapa = estado_conversa["etapa"]

    if etapa == "nome":
        estado_conversa["nome"] = mensagem
        estado_conversa["etapa"] = "telefone"
        return MENSAGENS["telefone"]

    elif etapa == "telefone":
        estado_conversa["telefone"] = mensagem
        estado_conversa["etapa"] = "endereco"
        return MENSAGENS["endereco"]

    elif etapa == "endereco":
        estado_conversa["endereco"] = mensagem
        estado_conversa["etapa"] = "menu"
        return mostrar_cardapio()

    elif etapa == "menu":
        item_escolhido = mensagem.strip().lower()
        item_encontrado = next((item for item in CARDAPIO if item['nome'].lower() == item_escolhido), None)

        if item_encontrado:
            estado_conversa["pedido"].append(item_encontrado)
            return f"Item '{item_encontrado['nome']}' adicionado. Deseja mais alguma coisa? Se não, digite 'finalizar'."
        elif mensagem.lower() == "finalizar":
            total = sum(item['preco'] for item in estado_conversa["pedido"])
            tempo_preparo, tempo_entrega = calcular_tempo_entrega(total)
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
        else:
            return "Item não encontrado. Digite o nome exato do produto como no cardápio ou 'finalizar'."

def mostrar_cardapio():
    mensagem = "CARDÁPIO:\n"
    for item in CARDAPIO:
        mensagem += f"- {item['nome']} - R$ {item['preco']:.2f}\n"
    mensagem += "\nDigite o nome do item que deseja ou 'finalizar'."
    return mensagem
