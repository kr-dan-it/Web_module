import sqlite3
connection = sqlite3.connect("store.db")

cursor = connection.cursor()
cursor.execute("Select * from users;")
print(cursor.fetchall())