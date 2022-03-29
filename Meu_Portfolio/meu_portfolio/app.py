import Portfolio.Estudos_code_show.db as db
from flask import Flask, abort, url_for

app = Flask(__name__)


# @app.route('/') #decorator
# def index():
#     html = ['<ul>']
#     for username, user in db.users.items():
#         html.append(
#             f'<li><a href="/{username}">{user["name"]}</a></li>'
#         )
#     html.append('</ul>')
#     return '\n'.join(html)

@app.route('/') #decorator
def index():
    html = ['<ul>']
    for username, user in db.users.items():
        html.append(
            f'<li><a href="{url_for("user", username=username)}">{user["name"]}</a></li>' # passa o nome do endpoint ao inves da url
            )
    html.append('</ul>')
    return '\n'.join(html)


def profile(username):
    user = db.users.get(username)

    if user:
        return f"""
        <h1>{user["name"]}</h1>
        <p>Age: {user["age"]}</p>
        <p>Location: {user["location"]}</p>
        <p>Telephone: {user["telephone"]}</p>
        <a href="/">Voltar</a>"""
    else:
        return abort(404, f'User {username} not found')


app.add_url_rule('/user/<username>/', view_func=profile, endpoint='user') #voce é obrigado a declarar o view ou endpoint e coloque a barra
   

app.run(use_reloader=True)

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
# caminhos, rotas, /user/<username>/ <- elemento dinamicos

# metodo route (
# rule= '/user/<username>/'
# view= 'python_function_name
# methods= ['GET', 'POST']
# endpoint= 'pnome_unico
# defaults= {'username': 'default_username'}
# )