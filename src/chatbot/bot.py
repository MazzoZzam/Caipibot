from ..chatbot.mensagens import MENSAGENS
from ..database.cliente import inserir_cliente, obter_id
from ..data.cardapio import mostrar_cardapio
from ..database.pedido import inserir_pedido, atualizar_pedido, ver_aprovados
from ..algorithms.linked_list import LinkedList
from ..algorithms.queue import Queue

lista = LinkedList()
fila = Queue()

conversa = {
    "etapa": "nome",
    "nome_cliente": "",
    "telefone_cliente": "",
    "endereco": "",
    "pedidos": []
}

def processar_mensagem(mensagem):
    etapa = conversa["etapa"]
    etapa_atual = estado_conversa.get(etapa)

    if etapa_atual:
        return etapa_atual(mensagem)
    else:
        return "Não existe está etapa no processo"

def perguntar_nome(mensagem):
    conversa["nome_cliente"] = mensagem
    conversa["etapa"] = "telefone"
    return MENSAGENS["telefone"]

def perguntar_telefone(mensagem):
    conversa["telefone_cliente"] = mensagem
    conversa["etapa"] = "endereco"
    return MENSAGENS["endereco"]

def perguntar_endereco(mensagem):
    conversa["endereco"] = mensagem
    conversa["etapa"] = "menu"

    # obtendo informações do cliente
    nome = conversa.get("nome_cliente")
    telefone = conversa.get("telefone_cliente")
    endereco = conversa.get("endereco")

    # inserindo informações do cliente no banco
    inserir_cliente(nome, telefone, endereco)

    return ("Ótimo! Aqui está as minhas principais funções, em que poderei ser útil?" + apresentar_menu(""))

def apresentar_menu(mensagem):
    if not mensagem:
        return ("Escolha uma opção pelos números ou palavras-chaves: \n"
                "1️⃣ Fazer pedido \n"
                "2️⃣ Gerenciar pedidos \n"
                "3️⃣ Realizar pedidos processados \n"
                "4️⃣ Ver pedidos aprovados")

    op = mensagem.strip().lower()

    if op == "1" or "fazer" in op:
        conversa["etapa"] = "fazer_pedido"   	 
        return fazer_pedido(mensagem)
    
    elif op == "2" or "ver" in op:
        conversa["etapa"] = "gerenciar_pedido"
        return gerenciar_pedido(mensagem)
    
    elif op == "3" or "gerenciar" in op:
        conversa["etapa"] = "realizar_pedido"
        return realizar_pedido(mensagem)
    
    elif op == "4" or "aprovados" in op:
        conversa["etapa"] = "pedidos_aprovados"
        return pedidos_aprovados(mensagem)

    else:
        return "Esta opção é invalida, tente novamente via números ou palavras-chave como 'fazer', 'ver', 'gerenciar' e 'aprovados'"

def fazer_pedido(mensagem):
    conversa["pedidos"] = []
    conversa["etapa"] = "item_escolhido"
    return ("Que bom que você quer fazer um pedido com a gente! Aqui está nosso cardápio: \n"
            f"{mostrar_cardapio()} \n"
            "Por favor selecione algum item por numero ou digite 'finalizar'")

def item_escolhido(mensagem):
    item = mensagem.strip().lower()
    pedidos = conversa["pedidos"]
    
    if item == "finalizar":
        if not pedidos:
            return "Nenhum item adicionado ao pedido"
        
        id_cliente = obter_id(conversa["nome_cliente"], conversa["telefone_cliente"], conversa["endereco"])

        inserir_pedido(id_cliente, pedidos)

        conversa["etapa"] = "menu"
        return "Pedido finalizado com sucesso! Retornando ao menu... \n" + apresentar_menu(mensagem)
    

    if int(item) > 0 and int(item) <= 30:
        pedidos.append(int(item))
        return f"Item: {item} adicionado com sucesso! Caso tenha concluido o pedido digite 'finalizar'"
    else:  
        return "Item não encontrado, tente novamente ou digite 'finalizar'"

def ver_pedido():
    listar_pedidos = lista.ver_pedido()

    if not listar_pedidos:
        return "Nenhum pedido foi feito para ser visualizado"

    resposta = "Certo aqui estão seus pedidos! \n"

    for pedido in listar_pedidos:
        resposta += f"""
        ID do pedido - {pedido['ID_pedido']}, \n
        Nome Cliente - {pedido['nome']}, \n
        Telefone - {pedido['telefone']}, \n
        Endereço - {pedido['endereco']}, \n
        Data do Pedido - {pedido['data_pedido']}, \n
        Itens - {', '.join(str(i) for i in pedido['itens_pedido'])}, \n
        Valor Total do Pedido - {pedido['valor_total']} \n
        *--------------------------*
        """

    return resposta

def gerenciar_pedido(mensagem):
    conversa["etapa"] = "escolher_pedido"

    resposta = ver_pedido()

    return ("Entendido vamos gerenciar os pedidos \n"
            "Esses são os pedidos disponíveis: \n"
            f"{resposta} \n"
            "O que deseja fazer com os pedidos?: \n"
            "1️⃣ Processar primeiro pedido \n"
            "2️⃣ Realizar ultimo pedido \n"
            "3️⃣ Realizar pedidos por id \n"
            "4️⃣ Voltar ao menu \n")

def escolher_pedido(mensagem):
    op = mensagem.strip().lower()

    if op == 1 or "inicio" in op:
        lista.processar_pedido_inicio()
        conversa["etapa"] = "menu"
        return ("Primeiro pedido processado com sucesso! \n"
                "Retornando ao menu..." + apresentar_menu(mensagem))

    elif op == 2 or "ultimo" in op:
        lista.processar_pedido_fim()
        conversa["etapa"] = "menu"
        return ("Ultimo pedido processado com sucesso! \n"
                "Retornando ao menu..." + apresentar_menu(mensagem))
    
    elif op == 3 or "id" in op:
        conversa["etapa"] = "aguardar_id"
        return "Por favor, digite o ID do pedido que deseja processar"
    
    elif op == 4 or "voltar" in op or "menu" in op:
        conversa["etapa"] = "menu"
        return "Retornando ao menu..." + apresentar_menu(mensagem)

    else:
        return "Opção invalida, tente novamente"

def aguardar_id(mensagem):

    id = int(mensagem.strip().lower())

    lista.processar_pedido(id)

    conversa["etapa"] = "menu"

    return "Retornando ao menu..." + apresentar_menu(mensagem)

def ver_processados():
    listar_pedidos = fila.ver_processamento()

    if not listar_pedidos:
        return "Nenhum pedido foi processado para ser visualizado"

    resposta = "Certo aqui estão seus pedidos em processo! \n"

    for pedido in listar_pedidos:
        resposta += f"""
        ID do pedido - {pedido[0]}, \n
        Nome Cliente - {pedido[1]}, \n
        Telefone - {pedido[2]}, \n
        Endereço - {pedido[3]}, \n
        Data do Pedido - {pedido[4]}, \n
        Itens - {', '.join(str(i) for i in pedido[5])}, \n
        Valor Total do Pedido - {pedido[6]} \n
        *--------------------------*
        """

    return resposta

def realizar_pedido(mensagem):
    conversa["etapa"] = "processar_pedido"

    fila_id = fila.obter_id_fila()

    return ("Entendido vamos realizar os pedidos \n"
            "Esses são os pedidos em processamento: \n"
            f"{ver_processados()} \n"
            f"Você deseja atualizar o pedido: {fila_id} como pronto?"
            "1️⃣ - Sim \n"
            "2️⃣ - Nao \n")

def processar_pedido(mensagem):
    op = mensagem.strip().lower()
    id_pedido = fila.obter_id_fila

    if op == 1 or "sim" in op:
        fila.processar_pedido()

        atualizar_pedido(id_pedido)

        conversa["etapa"] = "menu"

        return "Pedido realizado com sucesso! Retornando ao menu..." + apresentar_menu(mensagem)
    elif op == 2 or "nao" in op:
        return "Retornando ao menu..." + apresentar_menu(mensagem)
    else: 
        return "Opção invalida, tente novamente"

def pedidos_aprovados(mensagem):
    conversa["etapa"] = "menu"

    aprovados = ver_aprovados()

    if not aprovados:
        return "Nenhum pedido aprovado, retornando ao menu..." + apresentar_menu(mensagem)

    return ("Aqui estão os pedidos que foram aprovados para entrega! \n"
            f"{aprovados} \n"
            "Retornando ao menu..." + apresentar_menu(mensagem))

# dicionario do estado da conversa
estado_conversa = {
    "nome": perguntar_nome,
    "telefone": perguntar_telefone,
    "endereco": perguntar_endereco,
    "menu": apresentar_menu,
    "fazer_pedido": fazer_pedido,
    "item_escolhido": item_escolhido,
    "ver_pedido": ver_pedido,
    "gerenciar_pedido": gerenciar_pedido,
    "escolher_pedido": escolher_pedido,
    "aguardar_id": aguardar_id,
    "realizar_pedido": realizar_pedido,
    "aguardar_input": processar_pedido,
    "pedidos_aprovados": pedidos_aprovados  
}