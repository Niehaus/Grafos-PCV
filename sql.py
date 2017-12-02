import sqlite3

#cria um novo banco, se ainda nao existir
with sqlite3.connect("blog.db") as connection:

    #pega o caminho do objeto usado pelo SQL
    c = connection.cursor()

    #cria as tabelas
    c.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")

    #insere os valores na tabela
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well")')
    c.execute('INSERT INTO posts VALUES("Excelente", "I\'m excelent")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay")')