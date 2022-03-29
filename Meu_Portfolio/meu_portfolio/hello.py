__version__ = '0.1.0'
from flask import Flask

app = Flask(__name__) # primeiro argumento

@app.route("/")#decorador para informar ao Flask qual URL deve acionar nossa função
def hello_world(): # a função retorna a mensagem que queremos exibir no navegador do usuario, além disso o tipo de conteudo padrão é HTML, portanto, o HTML na string será renderizado pelo navegador.
    return "<p>Hello, World!</p>"