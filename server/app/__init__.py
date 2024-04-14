from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from auth import auth_bp
from . import *

db = SQLAlchemy()

app = Flask(__name__)
# Use other configurations from Config class
app.config.from_object(Config)

app.register_blueprint(auth_bp)

db.init_app(app)

from .views import *  # Import the api blueprint
from .models import *

with app.app_context():
    db.create_all()

