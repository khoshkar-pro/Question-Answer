from application import app, user_session, db_get
from flask import render_template

@app.route('/user-setup')
def user_setup():
    user = user_session()
    db = db_get()
    curr = db.execute('SELECT id,name, expert, admin FROM users')
    result = curr.fetchall()
    return render_template('userSetup.html', title='Set users permission', user=user, result=result)