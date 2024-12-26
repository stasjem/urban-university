import sqlite3



def initiate_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER
    )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        ''')

    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * FROM Products
        ''')
    total2 = cursor.fetchall()
    connection.commit()
    connection.close()
    return total2

def set_all_products():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    for i in range(1, 6):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (f"title{i}", f"description{i}", f"price{i}"))
    cursor.fetchall()
    connection.commit()
    connection.close()

def add_user(username, email, age):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))

    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT username FROM Users WHERE username = ?", (username, ))
    total2 = cursor.fetchone()
    connection.commit()
    connection.close()

    if not total2:
        return False
    else:
        return True