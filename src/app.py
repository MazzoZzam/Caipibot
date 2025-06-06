from flask import Flask, render_template, request, jsonify
from src.database.conexao import engine, meta
from src.data import cardapio
from src.database import cliente, pedido
from src.chatbot.bot import processar_mensagem

# Aplicativo Flask
app = Flask(__name__)

try:
    meta.create_all(engine)
    print("banco de dados mepeado com sucesso!")
except Exception as e:
    print(f"Algo deu errado durante o mapeamento do banco: {e}")

if cardapio.verificar_cardapio() < 30:
    cardapio.criar_cardapio()
    print("cardapio iniciado")
else:
    print("cardapio ja existe")

try:
    pedido.inserir_pedido_lista()
    print("Reinserindo pedidos a lista")
except Exception as e:
    print(f"Algo deu errado durante a inserção de pedidos a lista: {e}")

# Rota do site, serve o arquivo index.html
@app.route('/')
def index():
    return render_template('index.html')

# Receber, processar e enviar resposta do usuario
@app.route('/responder', methods=['POST'])
def responder():
    mensagem = request.json['mensagem']
    resposta = processar_mensagem(mensagem)
    return jsonify({'resposta': resposta})

if __name__ == '__main__':
    app.run(debug=True)
