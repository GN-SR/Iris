import sqlite3

conn = sqlite3.connect("iris.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(100))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'','')"
cursor.execute(query)
conn.commit()