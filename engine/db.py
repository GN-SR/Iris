import sqlite3

conn = sqlite3.connect("iris.db")
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(100))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'whatsapp','C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2445.7.0_x64__cv1g1gvanyjgm\\WhatsApp.exe')"
cursor.execute(query)
conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(100))"
cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'chat gpt','https://chatgpt.com/')"
#cursor.execute(query)
#conn.commit()
