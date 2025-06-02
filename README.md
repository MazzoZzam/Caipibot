# Caipibot

O Caipibot é um projeto de desenvolvimento de um chatbot para gerenciar pedidos de bares e adegas, usando tecnologias de lista e fila encandeada para facilitar esse processo.

## Objetivo

Nosso objetivo principal é facilitar o registro e gestão dos pedidos para os donos de bares, trazendo informações como, dados do cliente, valor total e os itens, assim oferencendo mais controle sobre os pedidos feitos.
Para simular os pedidos chegando de forma sequencial, usamos uma lista dinâmica onde os pedidos chegam como uma fila (pelo final da lista), e assim o dono pode escolher, em qualquer posição da lista, retirar o pedido e mandar para fila de processamento, a fila de processamento vai servir para os pedidos que estão sendo preparados, quando o pedido estiver pronto o dono do bar pode atualizar o pedido, atualizando como aprovado.

## Tecnologias Utilizadas

Esse projeto está sendo desenvolvido em Python na versão 3.10.11, com uso de Flask para criar um servidor web

Para o Banco de Dados usamos MySQL/MariaDB para montar o banco, e para integrar no código usamos a framework SQLAlchemy para mapear e fazer as operações de CRUD no código.

A interface foi feita usando HTML, CSS e JS
Aqui está a lista das tecnologias que usamos

- Python 3.10.11
- Flask
- MySQL - SQLAlchemy
- HTML, CSS e JS

## Estrutura do Projeto

Caipibot
├── rasa-project/
├── src
│ ├── algorithms/
│ │ ├── --init--.py
│ │ ├── linked_list.py
│ │ └── queue.py
│ ├── chatbot/
│ │ ├── --init--.py
│ │ ├── chatbot.py
│ │ └── mensagens.py
│ ├── data/
│ │ └── cardapio.py
│ ├── database/
│ │ ├── --init--.py
│ │ ├── cliente.py
│ │ ├── conexao.py
│ │ └── pedido.py
│ ├── static/
│ │ ├── fundo.jpeg
│ │ ├── icon.png
│ │ ├── script.js
│ │ └── style.css
│ ├── template/
│ │ └── index.html
│ ├── --init--.py
│ └── app.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

## Como executar

Se quiser utilizar corretamente no seu computador, clone o repositório (ou baixe o zip), e crie o Ambiente Virtual Python (venv) assim como criar apenas o Banco de Dados, apenas o banco de dados, ao executar o programa ele automaticamente vai criar as tabelas.

1. Clonando o repositório:

- No seu terminal digite:

```
git clone https://github.com/MazzoZzam/Caipibot.git
cd caipibot
```

2. Criando e ativando o ambiente virtual:

```
python -m venv .venv
.venv\Scripts\activate.bat
```

3. Instalando as dependências:

```
pip install -r requirements.txt
```

4. Crie o banco de dados no localhost:

- Abra seu mysql ou banco de dados de preferência e execute:

```
mysql -u root
CREATE DATABASE caipibot_database;
```

5. Execute o aplicativo (em uma pasta anterior ao src):

```
python -m src.app
```

## Equipe

- Matheus Akira Saito de Souza | https://github.com/MazzoZzam
- William Souza da Silva
- José Gonçalvez Braz Junior

## Disciplinas Envolvidas

- Estrutura de Dados I
- Banco de Dados

## Informações Acadêmicas

- Universidade: **Centro Universitário Braz Cubas**
- Curso: **Ciência da Computação**
- Semestre: 3º e 2º
- Professora orientadora: **Dra. Andréa Ono Sakai**
- Evento: **Mostra de Tecnologia 1º Semestre de 2025**
- Local: Laboratório 12
- Data: 05 de junho de 2025

## Licença

MIT License - Utilize, estude e modifique o código o quanto quiser, desde que não seja para fins comerciais sem autorização.
