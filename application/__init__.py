from flask import Flask, g
app = Flask(__name__, template_folder='templates')
app.config['DEBUG'] = True

from application.routes import home