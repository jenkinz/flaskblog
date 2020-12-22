"""
__init__.py
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "3dd5f41b4515718150c7b360b0f9bbab"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  # file relative to project dir
db = SQLAlchemy(app=app)

from flaskblog import routes
