import sqlite3
import random

conn = sqlite3.connect('tuto.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS lookMyHorse1(id REAL,nome TEXT,gen TEXT,age INT) ')

def entry():
    id = random.randrange(0, 1000)
    nome = str(input('Digite seu nome: '))
    gen = str(input('[M] [F]: ')).upper()
    age = int(input('Sua idade: '))
    c.execute("INSERT INTO lookMyHorse1 (id, nome, gen, age) vALUES (?, ? , ?, ?)",
              (id, nome, gen, age))
    conn.commit()

create_table()

while True:
    entry()
    a = str(input('Inserir novos dados? '))
    if a not in 'sS':
        break

