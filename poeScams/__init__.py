from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gems.db'
app.config['SECRET_KEY'] = '9bccab9f134819d14a9a73a0'
db = SQLAlchemy(app)
# This forces the current application
app.app_context().push()

from poeScams import routes
