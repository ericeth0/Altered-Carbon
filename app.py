from crypt import methods
from flask import Flask, jsonify, request  # Puxando o que vai ser usado

app = Flask(__name__)  # Criar um app flask de hospedagem API

livros = [
    {
        'id': 1,
        'titulo': 'Neuromancer - Sprawl trilogy',
        'Author': 'William Gibson'
    },
    {
        'id': 2,
        'titulo': 'Count Zero - Sprawl trilogy',
        'Author': 'William Gibson'
    },
    {
        'id': 3,
        'titulo': 'Monalisa Overdrive - Sprawl trilogy',
        'Author': 'William Gibson'
    }
]


# Consultar (All)
# Quero que apenas o GET seja utilizado nessa function
@app.route('/livros', methods=['GET'])
def get_books():
    return jsonify(livros)  # retornar em formato json


# Consultar (ID)
# especificando um inteiro com a palavra chave id
@app.route('/livros/<int:id>', methods=['GET'])
def get_book_id(id):
    for livro in livros:
        if livro.get('id') == id:  # pegar a prop id nos livros
            return jsonify(livro)


# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def edit_books(id):
    altered_carbon = request.get_json()  # pega as infos já enviadas
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            # altera o livro indexado do indice
            livros[indice].update(altered_carbon)
            return jsonify(livros[indice])


# Criar um livro novo
@app.route('/livros', methods=['POST'])
def create_book():
    new_book = request.get_json()
    livros.append(new_book)
    return jsonify(livros)


# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_book(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livro[indice]  # excluindo o livro do indice

    return jsonify(livros)  # retornar os livros restantes


app.run(port=5000, host='localhost', debug=True)  # rodando a aplicação
