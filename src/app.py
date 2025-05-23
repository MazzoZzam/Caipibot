from flask import Flask, render_template, request, jsonify
from chatbot.bot import processar_mensagem

# Aplicativo Flask
app = Flask(__name__)

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
