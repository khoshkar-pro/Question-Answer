from flask import redirect, session, url_for
from application import app

@app.route('/logout')
def logout():
    session.pop('user_session', None)
    return redirect(url_for('home'))