class Node:
    def __init__(self, id = 0, prox = None):
        self.id = id
        self.prox = prox

class Queue:
    def __init__(self):
        self.comeco = None
        self.final = None

    def receber_pedido(self, id):
        node = Node(id, None)
                
        if self.comeco is None and self.final is None:    
            self.comeco = node
            self.final = node
            return
        
        self.final.prox = node
        self.final = self.final.prox
    
    def ver_processamento(self):
        if self.comeco is None:
            print("Nao tem nenhum pedido em processamento para visualizar")
            return
        
        itera = self.comeco
        print("Mostrando pedidos processados")
        while itera:
            print(f"Pedido id = {itera.id}")
            print("------------------------")
            itera = itera.prox

    def processar_pedido(self):
        if self.comeco is None:
            print("Nao tem nenhum pedido para preparar")
            return
        
        itera = self.comeco

        print(f"O pedido: {itera.id}, sera atualizado como pronto")
        con = int(input("Deseja continuar? (1 - Sim | 2 - Nao) "))

        if con == 1:
            self.comeco = itera.prox
            print("Pedido realizado com sucesso!")