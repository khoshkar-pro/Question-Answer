from application import app, user_session, db_get
from flask import render_template, redirect, url_for

@app.route('/user-setup')
def user_setup():
    user = user_session()
    if not user:
        return redirect(url_for('register'))
    if user['admin'] == 0:
        return redirect(url_for('home'))
    db = db_get()
    curr = db.execute('SELECT id,name, expert, admin FROM users')
    result = curr.fetchall()
    return render_template('userSetup.html', title='Set users permission', user=user, result=result)