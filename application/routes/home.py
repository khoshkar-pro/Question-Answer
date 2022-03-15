from application import app, user_session
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    user = user_session()
    return render_template('home.html', title='Home', user = user)