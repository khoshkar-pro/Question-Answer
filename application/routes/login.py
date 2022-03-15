from application import app, db_get
from flask import render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash

@app.route('/login', methods=['POST', 'GET'])
def login():
    db = db_get()
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user_curr = db.execute('SELECT id, name, password FROM users WHERE name = ?', [name])
        user_result = user_curr.fetchone()
        if check_password_hash(user_result['password'], password):
            session['user_session'] = user_result['name']
            return redirect(url_for('home'))
        else:
            return render_template('login.html', title='Login', incorrect_password=True)
    return render_template('login.html', title = 'Login')