from application import app, db_get, user_session
from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

@app.route('/register', methods=['POST', 'GET'])
def register():
    user = user_session()
    db = db_get()
    if request.method == 'POST':
        check_user_curr = db.execute('SELECT name from users WHERE name = ?', [request.form['name']])
        check_user = check_user_curr.fetchone()
        if check_user:
            return redirect(url_for('register'))
        hashed_pass = generate_password_hash(request.form['password'], method='sha256')
        db.execute('INSERT INTO users (name, password, expert, admin) values (?, ?, ?, ?)', [request.form['name'], hashed_pass, '0', '0'])
        db.commit()
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', user=user)