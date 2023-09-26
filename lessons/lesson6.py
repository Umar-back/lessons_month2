# база данных
# ветки git pull
# sql
# субд - система управления базами данных
# MYsql posgreSQL Sqlite3

# str float int bool {} [] ()

import sqlite3
database = sqlite3.connect('test.database')
c = database.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS students(
name TEXT,
age INTEGER,
view INTEGER,
hobby TEXT DEFAULT 0
)''')
c.execute('''INSERT INTO students VALUES ('sali',12,4,0)''')


database.commit()
database.close()