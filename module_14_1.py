import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1,11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i}0", "1000"))


ids = cursor.execute('SELECT id FROM Users').fetchall()
for id in ids:
    if (id[0] - 1) % 2 == 0:
        cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (id[0],))

ids = cursor.execute('SELECT id FROM Users').fetchall()
for id in ids:
    if (id[0] - 1) % 3 == 0:
        cursor.execute('DELETE FROM Users WHERE id = ?', (id[0],))



cursor.execute("SELECT * FROM Users WHERE age <> 60")
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')


cursor.close()
connection.commit()
connection.close()
