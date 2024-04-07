from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


db = SQLAlchemy()

app = Flask(__name__)

# Use other configurations from Config class
app.config.from_object(Config)

db.init_app(app)

from .routes import *
from .models import *

with app.app_context():
    db.create_all()