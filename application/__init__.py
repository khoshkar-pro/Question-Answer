from flask import Flask, g, render_template, session
import sqlite3, os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(15).hex()

# database initialization
def db_conn():
    sql = sqlite3.connect(r'C:\Users\Khoshkar\PycharmProjects\Question-Answer\application\database\database.db')
    sql.row_factory = sqlite3.Row
    return sql
def db_get():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = db_conn()
    return g.sqlite_db

@app.teardown_appcontext
def db_close(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', title='Not found'), 404

def user_session():
    user = None
    if 'user_session' in session:
        user = session['user_session']
        return user

from application.routes import home
from application.routes import register
from application.routes import login
from application.routes import logout