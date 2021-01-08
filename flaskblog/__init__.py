"""
__init__.py
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config["SECRET_KEY"] = "3dd5f41b4515718150c7b360b0f9bbab"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  # file relative to project dir
db = SQLAlchemy(app=app)
bcrypt = Bcrypt(app=app)
login_manager = LoginManager(app)
login_manager.login_view = "login"  # this is the redirect if a 'login_required' route is hit and user is not logged in
login_manager.login_message_category = "info"

from flaskblog import routes
