from ..algorithms.queue import fila

class Node:
    def __init__(self, id = 0, 
                 nome = "", 
                 tel = "", 
                 end = "",
                 data_pedido = "", 
                 pedidos = [], 
                 preco_total = 0, 
                 prox = None):
        self.id = id
        self.nome = nome
        self.tel = tel
        self.end = end
        self.data_pedido = data_pedido
        self.pedidos = pedidos
        self.preco_total = preco_total
        self.prox = prox

class LinkedList:    
    def __init__(self):
        self.inicio = None

    def novo_pedido(self, id, nome, tel, end, data_pedido, pedidos, preco_total): 

        if self.inicio is None:
            self.inicio = Node(id, nome, tel, end, data_pedido, pedidos, preco_total, None)
            return
        
        itera = self.inicio

        while itera.prox:
            itera = itera.prox
        
        itera.prox = Node(id, nome, tel, end, data_pedido, pedidos, preco_total, None)

        return

    def ver_pedido(self): 
        if self.inicio is None:
            return "" 

        lista_pedidos = [] 
        itera = self.inicio
        while itera:
            pedidos = {
                "ID_pedido": itera.id,
                "nome": itera.nome,
                "telefone": itera.tel,
                "endereco": itera.end,
                "data_pedido": itera.data_pedido,
                "itens_pedido": itera.pedidos,
                "valor_total": itera.preco_total
            }
            lista_pedidos.append(pedidos)
            itera = itera.prox

        return lista_pedidos

    def processar_pedido_inicio(self):
        if self.inicio is None:
            return ("A lista de pedidos esta vazia")
            
        itera = self.inicio

        fila.receber_pedido(itera.id, itera.nome, itera.tel, itera.end, itera.data_pedido, itera.pedidos, itera.preco_total)
        itera = itera.prox

        self.inicio = itera

        return

    def processar_pedido_fim(self):
        if self.inicio is None:
            return ("A lista de pedidos esta vazia")
            
        itera = self.inicio
        ant = None

        if itera.prox is None:
            fila.receber_pedido(itera.id, itera.nome, itera.tel, itera.end, itera.data_pedido, itera.pedidos, itera.preco_total)
            return

        while itera.prox:
            ant = itera
            itera = itera.prox

        fila.receber_pedido(itera.id, itera.nome, itera.tel, itera.end, itera.data_pedido, itera.pedidos, itera.preco_total)
        ant.prox = None

        return

    def processar_pedido(self, id):
        itera = self.inicio
        ant = None

        if self.inicio is None:
            return ("A lista de pedidos esta vazia")
            
        elif self.inicio.id == id:
            self.inicio = itera.prox
            fila.receber_pedido(itera.id, itera.nome, itera.tel, itera.end, itera.data_pedido, itera.pedidos, itera.preco_total)
            return
        
        while itera.id != id:
            if itera is None:
                return "ID do pedido não existe, por favor tente novamente"
            
            ant = itera
            itera = itera.prox
        

        fila.receber_pedido(itera.id, itera.nome, itera.tel, itera.end, itera.data_pedido, itera.pedidos, itera.preco_total)
        ant.prox = itera.prox

        return
    

lista = LinkedList()