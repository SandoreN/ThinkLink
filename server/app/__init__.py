from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()  # This loads the environment variables from a .env file


# Create the Flask application
app = Flask(__name__)

# Initialize extensions but don't associate them with the app yet
db = SQLAlchemy()

# Apply configuration
from .config import Config  # Ensure config is in the same directory or properly referenced
app.config.from_object(Config)
print(app.config['SQLALCHEMY_DATABASE_URI'])  # This should print the URI if set


# Setup CORS
CORS(app, origins=['http://localhost:8080'])

# Import blueprints and models after app and db are defined
from .auth import auth_bp  # Assuming auth_bp is defined in the auth module

# Register blueprints
app.register_blueprint(auth_bp)

# Initialize SQLAlchemy with the app
db.init_app(app)

# Assuming that views and models modules don't cause circular imports
from .views import *
from .models import *

with app.app_context():
    db.create_all()


