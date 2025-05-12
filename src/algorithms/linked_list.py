class Node:
    def __init__(self, id = 0, prox = None):
        self.id = id
        self.prox = prox

class LinkedList:
    def __init__(self):
        self.inicio = None
    
    def novo_pedido(self, id):
        if self.inicio is None:
            self.inicio = Node(id, None)
            return
        
        itera = self.inicio

        while itera.prox:
            itera = itera.prox
        
        itera.prox = Node(id, None)

    def ver_pedido(self):
        if self.inicio is None:
            print("Nao tem nenhum pedido para visualizar")
            return
        
        itera = self.inicio
        print("Mostrando pedidos")
        while itera:
            print(f"Pedido id = {itera.id}")
            print("------------------------")
            itera = itera.prox

    def preparar_pedido_inicio(self):
        if self.inicio is None:
            print("A lista de pedidos esta vazia")
            return
        
        itera = self.inicio

        itera = itera.prox

        self.inicio = itera

    def preparar_pedido_fim(self):
        if self.inicio is None:
            print("A lista de pedidos esta vazia")
            return
        
        itera = self.inicio
        ant = None

        while itera.prox:
            ant = itera
            itera = itera.prox

        ant.prox = None

    def preparar_pedido(self, id):
        itera = self.inicio
        ant = None
        
        if self.inicio.id == id:
            self.inicio = itera.prox
            return
        
        while itera.id != id:
            ant = itera
            itera = itera.prox

        ant = itera.prox 
        
        




def main():
    print("teste")
    lista = LinkedList()
    lista.novo_pedido(30)
    lista.novo_pedido(31)
    lista.novo_pedido(32)
    lista.novo_pedido(33)
    lista.ver_pedido()
    lista.preparar_pedido(32)
    lista.ver_pedido()
    


if __name__ == '__main__':
    main()