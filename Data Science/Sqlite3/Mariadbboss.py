import sqlite3
import time
import datetime
import random
import matplottlib.pyplot as plt

conn = sqlite3.connect('tuto.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS lookMyHorse(unix REAL, datestamp TEXT, keyword TEXT, value REAL) ')

def data_entry():
    c.execute("INSERT INTO lookMyHorse VALUES('454515151515', '2016-01-01', 'Python', '5' )")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO lookMyHorse (unix, datestamp, keyword, value) vALUES (?, ? , ?, ?)",
              (unix,date,keyword,value))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM lookMyHorse')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)

"""create_table()
data_entry()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1) """
#read_from_db()

c.close()
conn.close()