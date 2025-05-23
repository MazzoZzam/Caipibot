from ..algorithms.queue import *
from ..data.cardapio import CARDAPIO

class Node:
    def __init__(self, id = 0, pedidos = [], quant = 0, preco_total = 0, prox = None):
        self.id = id
        self.pedidos = pedidos
        self.quant = quant
        self.preco_total = preco_total
        self.prox = prox

class LinkedList:    
    def __init__(self):
        self.inicio = None

    def novo_pedido(self, id, pedido, quant, preco_total): 

        if self.inicio is None:
            self.inicio = Node(id, pedido, quant, preco_total, None)
            return
        
        itera = self.inicio

        while itera.prox:
            itera = itera.prox
        
        itera.prox = Node(id, pedido, quant, preco_total, None)

    def ver_pedido(self):
        if self.inicio is None:
            print("Nao tem nenhum pedido para visualizar")
            return
        
        itera = self.inicio
        print("Mostrando pedidos")
        while itera:
            print(f"Pedido id: {itera.id}")
            for item in itera.pedidos:
                print(f"itens: {CARDAPIO[item]['nome']} ")
            print(f"Quantidade: {itera.quant}")
            print(f"Total: {itera.preco_total}")
            print("------------------------")
            itera = itera.prox

    def processar_pedido_inicio(self):
        if self.inicio is None:
            print("A lista de pedidos esta vazia")
            return
        
        itera = self.inicio

        fila.receber_pedido(itera.id, itera.pedidos, itera.quant, itera.preco_total)

        itera = itera.prox

        self.inicio = itera

    def processar_pedido_fim(self):
        if self.inicio is None:
            print("A lista de pedidos esta vazia")
            return
        
        itera = self.inicio
        ant = None

        while itera.prox:
            ant = itera
            itera = itera.prox

        fila.receber_pedido(itera.id, itera.pedidos, itera.quant, itera.preco_total)
        ant.prox = None

    def processar_pedido(self, id):
        itera = self.inicio
        ant = None

        if self.inicio is None:
            print("A lista de pedidos esta vazia")
            return 
        elif self.inicio.id == id:
            self.inicio = itera.prox
            fila.receber_pedido(itera.id, itera.pedidos, itera.quant, itera.preco_total)
            return
        
        while itera.id != id:
            ant = itera
            itera = itera.prox

        fila.receber_pedido(itera.id, itera.pedidos, itera.quant, itera.preco_total)
        ant.prox = itera.prox 

lista = LinkedList()
fila = Queue() 

def main():
    index = 0
    pedido = []
    quant = 0
    preco_total = 0

    for item in CARDAPIO:
        print(f"{index}. {item['nome']} - Preco: R${item['preco']}")
        index += 1

    print("faca seu pedido ai:")
    print("--------------------")

    pedido = [12, 13, 14]
    quant = len(pedido)
    for item in pedido:
        preco_total += CARDAPIO[item]['preco']

    lista.novo_pedido(1, pedido, quant, preco_total)

    preco_total = 0
    pedido = [21, 22, 23, 20]
    quant = len(pedido)
    for item in pedido:
        preco_total += CARDAPIO[item]['preco']

    lista.novo_pedido(2, pedido, quant, preco_total)

    lista.ver_pedido()

    lista.processar_pedido()

    lista.ver_pedido()
    fila.ver_processamento()
    fila.processar_pedido()
    fila.ver_processamento()

    
   


if __name__ == '__main__':
    main()