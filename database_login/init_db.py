import sqlite3

# Connect ke database (bakal bikin file users.db otomatis)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Bikin tabel user
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Tambah user dummy buat ngetes login (User: admin, Pass: 123)
try:
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', '123'))
    conn.commit()
    print("Database & User dummy berhasil dibuat!")
except:
    print("User udah ada.")

conn.close()

