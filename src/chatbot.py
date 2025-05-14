
import time

class Chatbot:
    def __init__(self):
        self.stage = "start"
        self.user_info = {
            "nome": "",
            "telefone": "",
            "endereco": "",
            "pedido": []
        }
        self.cardapio = {
            "Caipirinha Clássica": 20.0,
            "Caipiroska": 25.0,
            "Caipirinha de Morango": 22.0,
            "Caipirinha de Maracujá": 22.0,
            "Caipirinha sem Álcool": 15.0
        }

    def process_input(self, user_input):
        if self.stage == "start":
            self.stage = "get_nome"
            return "Olá! Qual o seu nome?"

        elif self.stage == "get_nome":
            self.user_info["nome"] = user_input
            self.stage = "get_telefone"
            return f"Prazer, {user_input}! Qual o seu telefone?"

        elif self.stage == "get_telefone":
            self.user_info["telefone"] = user_input
            self.stage = "get_endereco"
            return "Qual o seu endereço para entrega?"

        elif self.stage == "get_endereco":
            self.user_info["endereco"] = user_input
            self.stage = "mostrar_cardapio"
            return self.mostrar_cardapio()

        elif self.stage == "mostrar_cardapio":
            item = user_input.strip()
            if item in self.cardapio:
                self.user_info["pedido"].append(item)
                return f"{item} adicionado ao pedido. Deseja mais alguma coisa? Se não, digite 'finalizar'."
            elif item.lower() == "finalizar":
                self.stage = "finalizar"
                return self.finalizar_pedido()
            else:
                return "Item não reconhecido. Por favor, escolha um item do cardápio ou digite 'finalizar'."

        elif self.stage == "finalizar":
            return "Pedido já finalizado. Recarregue a página para um novo pedido."

        return "Desculpe, não entendi. Por favor, tente novamente."

    def mostrar_cardapio(self):
        cardapio_texto = "CARDÁPIO:"
        for item, preco in self.cardapio.items():
            cardapio_texto += f"- {item}: R$ {preco:.2f}"
            
        cardapio_texto += "Digite o nome do item que deseja pedir."
        return cardapio_texto

    def finalizar_pedido(self):
        total = sum(self.cardapio[item] for item in self.user_info["pedido"])
        tempo = self.calcular_tempo(total)
        mensagem = f"Pedido de {self.user_info['nome']} finalizado!"
        mensagem += f"Telefone: {self.user_info['telefone']}"
        mensagem += f"Endereço: {self.user_info['endereco']}"
        mensagem += f"Itens pedidos: {', '.join(self.user_info['pedido'])}"
        mensagem += f"Total: R$ {total:.2f}"
        mensagem += f"Tempo estimado: preparo {tempo} min e entrega {tempo} min."
        mensagem += "Iniciando preparo..."

        time.sleep(tempo)
        mensagem += "Pedido pronto!"
        time.sleep(tempo)
        mensagem += "Pedido entregue!"
        return mensagem

    def calcular_tempo(self, total):
        if total <= 50:
            return 1
        elif total <= 100:
            return 2
        elif total <= 150:
            return 3
        else:
            return 5
