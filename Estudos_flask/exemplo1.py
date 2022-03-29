__version__ = '0.1.0'
from flask import Flask, jsonify

app = Flask(__name__) # primeiro argumento

@app.route("/")#decorador para informar ao Flask qual URL deve acionar nossa função
def hello_world(): # a função retorna a mensagem que queremos exibir no navegador do usuario, além disso o tipo de conteudo padrão é HTML, portanto, o HTML na string será renderizado pelo navegador.
    return "<p>Hello, World!</p>"


@app.route('/rota2')
def raiz():
    return '<H1>Essa é a segunda rota da aplicação</H1>'
    

@app.route('/pessoas/<string:nome>/<string:cidade>') #quando tem <> significa que é um parametro ou variavel
def pessoaa(nome, cidade):
    # return f'Nome: {nome}, Cidade: {cidade}'
    return jsonify({'nome': nome, 'cidade': cidade}) #retorna um arquivo json ao inves de html


app.run(debug=True)#muda o site em tempo real