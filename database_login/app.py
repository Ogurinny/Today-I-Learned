from flask import Flask, request, render_template_string
import sqlite3
from waitress import serve

app = Flask(__name__)

# Template HTML sederhana (biar lo gak usah bikin file .html dulu)
HTML_FORM = '''
    <h2>Login Form</h2>
    <form method="POST">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <button type="submit">Login</button>
    </form>
    <p>{{ msg }}</p>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        
        if user:
            msg = "✅ Login Berhasil! Halo, " + user[1]
        else:
            msg = "❌ Login Gagal. Coba lagi, bre."
        conn.close()
        
    return render_template_string(HTML_FORM, msg=msg)

if __name__ == "__main__":
    print("Server Waitress running on http://127.0.0.1:8080")
    # Di sinilah Flask dan Waitress digabung
    serve(app, host='0.0.0.0', port=8080, threads=4)

