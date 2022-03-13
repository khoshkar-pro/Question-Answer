from application import app, db_get
from flask import render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/register', methods=['POST', 'GET'])
def register():
    db = db_get()
    if request.method == 'POST':
        hashed_pass = generate_password_hash(request.form['password'], method='sha256')
        db.execute('INSERT INTO users (name, password, expert, admin) values (?, ?, ?, ?)', [request.form['name'], hashed_pass, '0', '0'])
        db.commit()
    return render_template('register.html', title='Register')