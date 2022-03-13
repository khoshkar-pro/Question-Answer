from application import app, db_get
from flask import render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/login', methods=['POST', 'GET'])
def login():
    db = db_get()
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user_curr = db.execute('SELECT password FROM users WHERE name = ?', [name])
        user_result = user_curr.fetchone()
        if check_password_hash(user_result['password'], password):
            return '{}'.format('Password is correct.')
        else:
            return '{}'.format('Password is incorrect.')
    return render_template('login.html', title = 'Login')