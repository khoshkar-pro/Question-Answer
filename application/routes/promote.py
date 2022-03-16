from application import app, db_get
from flask import redirect, url_for

@app.route('/promote/<user_id>')
def promote(user_id):
    db = db_get()
    db.execute('UPDATE users SET expert = 1 WHERE id = ?', [user_id])
    db.commit()
    return redirect(url_for('user_setup'))