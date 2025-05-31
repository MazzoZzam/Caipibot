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

class Queue:
    def __init__(self):
        self.comeco = None
        self.final = None

    def receber_pedido(self, id, nome, tel, end, data_pedido, pedidos, preco_total):
        node = Node(id, id, nome, tel, end, data_pedido, pedidos, preco_total, None)
                
        if self.comeco is None and self.final is None:    
            self.comeco = node
            self.final = node
            return
        
        self.final.prox = node
        self.final = self.final.prox
        return
    
    def ver_processamento(self):
        if self.comeco is None:
            return "Nao tem nenhum pedido para visualizar"
            
        lista_pedidos = [] 
        itera = self.comeco
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

    def processar_pedido(self):
        if self.comeco is None:
            return ("Nao tem nenhum pedido para preparar")
            
        itera = self.comeco

        self.comeco = itera.prox
        return

    def obter_id_fila(self):
        if self.comeco is None:
            return ("Nao tem nenhum pedido para preparar")
        
        itera = self.comeco

        return itera.id
           