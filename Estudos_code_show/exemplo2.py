'''(.venv) ➜  Portfolio git:(master) ✗ ls
Estudos_code_show  Estudos_flask  Meu_Portfolio  README.md
(.venv) ➜  Portfolio git:(master) ✗ Estudos_code_show 
(.venv) ➜  Estudos_code_show git:(master) ✗ ls
db.py  exemplo1.py  exemplo2.py  __pycache__
(.venv) ➜  Estudos_code_show git:(master) ✗ export FLASK_APP=exemplo2.py
(.venv) ➜  Estudos_code_show git:(master) ✗ flask shell
Python 3.10.2 (main, Mar 21 2022, 19:46:49) [GCC 9.4.0] on linux
IPython: 8.2.0
App: exemplo2 [production]
Instance: /home/luben/Documentos/GitHub/Luben/Portfolio/Portfolio/Estudos_code_show/instance
In [1]: app
Out[1]: <Flask 'exemplo2'>

In [2]:  COMANDO PARA EXECUTAR O APP FLASK NO TERMINAL'''



import db
from flask import Flask, abort, url_for

app = Flask(__name__)

#dentro do flask temos um objeto chamado route
# @app.route('/') #decorator
# def index():
#     html = ['<ul>']
#     for username, user in db.users.items():
#         html.append( # aqui é onde vai a url html que é identificada pela tag a
#             f'<li><a href="/{username}/">{user["name"]}</a></li>'
#         )
#     html.append('</ul>')
#     return '\n'.join(html)

@app.route('/') #decorador
def index():
    html = ['<ul>']
    for username, user in db.users.items():
        html.append(
            f'<li><a href="{url_for("user", username=username)}">{user["name"]}</a></li>' # chama a funcao e passa o nome do endpoint ao inves da url e recebe esse username
            )
    html.append('</ul>')
    return '\n'.join(html)


def profile(username):# Confere se username esta no banco de dados funciona se não da error 404
    user = db.users.get(username)

    if user:
        return f"""
        <h1>{user["name"]}</h1>
        <p>Age: {user["age"]}</p>
        <p>Location: {user["location"]}</p>
        <p>Telephone: {user["telephone"]}</p>
        <a href="/">Voltar</a>"""
    else:
        return abort(404, f'User {username} not found') # esse abort é um response que mostra erro http


app.add_url_rule('/user/<username>/', view_func=profile, endpoint='user') #metodo imperativo de chamar, voce é obrigado a declarar o view ou endpoint e coloque a barra
   

# app.run(use_reloader=True)

# @app.route('/hello')
# def hello(): #view
#     return 'Hello World!'


# @app.route('/hi')
# def hi():
#     return 'Hi!'




# Roteamento de urls no flask
# Url = uniform resource locator
# site ou dominio localhost
# porta tcp por onde esse dado ira trafegar
# caminhos, rotas, /user/*<username>/* <- elemento dinamico e pode mudar, alem de ter tambem querry strings e #ancora

#Regras do route
# metodo route (
# rule= '/user/<username>/'
# view= 'python_function_name # qualquer objeto invocavel
# methods= ['GET', 'POST']
# endpoint= nome_unico
# defaults= {'username': 'default_username'}
# )


@app.route('/user/<username>/<quote_id>/')
def quote(username, quote_id):
    user = db.users.get(username, {})