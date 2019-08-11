import sqlite3

print("hello database")


def create_table():
    connection = sqlite3.connect("test.db")
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, qty INTEGER, price REAL)")
    connection.commit()
    connection.close()


def insert(item, qty, price):
    connection = sqlite3.connect("test.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, qty, price))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect("test.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    connection.close()
    return rows


#insert("Water", 99, 0.99)


print(view())

