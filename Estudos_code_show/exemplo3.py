#conversores de url

import db
from converters import RegexConverter, ListConverter
from flask import Flask, abort, url_for

app = Flask(__name__)
app.url_map.converters['regex'] = RegexConverter
app.url_map.converters['list'] = ListConverter


@app.route('/') #decorador
def index():
    html = ['<ul>']
    for username, user in db.users.items():
        html.append(
            f'<li><a href="{url_for("user", username=username)}">{user["name"]}</a></li>' # chama a funcao e passa o nome do endpoint ao inves da url e recebe esse username
            )
    html.append('</ul>')
    return '\n'.join(html)


@app.route('/user/<list:usernames>/', endpoint= 'user') #decorador
def profile(usernames):# Confere se username esta no banco de dados funciona se não da error 404
    html = ''
    for username in usernames:
        user = db.users.get(usernames)

        if user:
            html += f"""
                <h1>{user["name"]}</h1>
                <p>Age: {user["age"]}</p>
                <p>Location: {user["location"]}</p>
                <p>Telephone: {user["telephone"]}</p>
                <a href="/">Voltar</a>
            """

    return html or abort(404, f'Users {usernames} not found') # esse abort é um response que mostra erro http


app.add_url_rule('/user/<username>/', view_func=profile, endpoint='user') #metodo imperativo de chamar, voce é obrigado a declarar o view ou endpoint e coloque a barra


@app.route('/user/<username>/<int:quote_id>/')#conversor de url int: str: float:
def quote(username, quote_id):
    user = db.users.get(username) #metodo get precisa receber um argumento default
    quote = user.get('quotes').get(quote_id)
    # try: #tratamento de excecao, porem voce esta consumindo recursos da sua aplicacao para fazer isso
    #     quote = user.get('quotes').get(int(quote_id))
    # except ValueError:
    #     quote = False
    if user and quote:
           return f"""
        <h1>{user["name"]}</h1>
        <p>Age: {user["age"]}</p>
        <p><q>{quote}<q></p>
        <a href="/">Voltar</a>"""
    else:
        return abort(404, f'User or quote not found') # esse abort é um response que mostra erro http


@app.route('/file/<path:filename>/')#http://127.0.0.1:5000/file/filename/desktop/.jpg/asefsdfsad/ conversor PATH vai aceitar qualquer caminho separado por barra
def file(filename):
    return f'Argumento recebido: {filename}'

@app.route("/reg/<regex('a.*'):name>/")# criamos o nosso conversor de url, dessa forma ele ira mostrar tudo que comeca com a
def reg(name):
    return f'Argumento iniciado com a letra a: {name}'

@app.route("/reg/<regex('b.*'):name>/")#regex = regular expression, regex(vai receber o argumento):
def reg_b(name):
    return f'Argumento iniciado com a letra b: {name}'


app.run(use_reloader=True)