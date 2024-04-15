from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()
app = Flask(__name__)

from app.auth import auth_bp

app.register_blueprint(auth_bp)

# Use other configurations from Config class
app.config.from_object(Config)

db.init_app(app)

from .views import *  # Import the api blueprint
from .models import *

with app.app_context():
    db.create_all()


