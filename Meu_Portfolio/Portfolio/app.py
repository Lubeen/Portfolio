from distutils.command.config import config
from webbrowser import get
from ext.site import main
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.secret_key = 'namaste'
mail_settings = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 465,
    'MAIL_USE_TLS': False,
    'MAIL_USE_SSL': True,
    'MAIL_USERNAME': os.getenv("EMAIL"),
    'MAIL_PASSWORD': os.getenv("SENHA")
}
app.config.update(mail_settings)
mail = Mail(app)

class Contato():
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send' , methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['nome'],
            request.form['email'],
            request.form['mensagem']
        )
        msg = Message(
            subject=f'{formContato.nome} te enviou uma mensagem no Portfolio',
            sender= app.config.get('MAIL_USERNAME'),
            recipientes = ['luan.bezerra.contato@gmail.com', app.config.get('MAIL_USERNAME')],
            body=f'''
            
            {formContato.nome} com o email {formContato.email} te enviou a seguinte mensagem:
            {formContato.mensagem}
            '''
        )
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    return redirect('/')