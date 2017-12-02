from flask import  Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3

#configuracao
DATABASE = 'blog.db'

app = Flask(__name__)

#Puxa as configuracoes para localizar as variaveis maiusculas
app.config.from_object(__name__)

#funcao para conectar com o bd
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)