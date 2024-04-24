from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

<<<<<<< HEAD
db = SQLAlchemy()


app = Flask(__name__)
CORS(app, origins=['http://localhost:8080'], supports_credentials=True)
# Use other configurations from Config class
app.config.from_object(Config)

print(f"Secret key: {app.secret_key}")

from flask import session

@app.before_request
def make_session_permanent():
    session.permanent = True
    
from app.auth import auth_bp
from app.routes import routes_bp
app.register_blueprint(auth_bp)
app.register_blueprint(routes_bp)



=======
load_dotenv()  # This loads the environment variables from a .env file


# Create the Flask application
app = Flask(__name__)
CORS(app)

# Initialize extensions but don't associate them with the app yet
db = SQLAlchemy()

# Apply configuration
from .config import Config  # Ensure config is in the same directory or properly referenced
app.config.from_object(Config)
print(app.config['SQLALCHEMY_DATABASE_URI'])  # This should print the URI if set


# Setup CORS
CORS(app, resources={r"/*": {"origins": "http://localhost:8081"}})

# Import blueprints and models after app and db are defined
from .auth import auth_bp  # Assuming auth_bp is defined in the auth module

# Register blueprints
app.register_blueprint(auth_bp)

# Initialize SQLAlchemy with the app
>>>>>>> 877966aa5120b70c87fb43d591acbba184ed2ef3
db.init_app(app)

# Assuming that views and models modules don't cause circular imports
from .views import *
from .models import *

user_view = CRUDView(model=User)

with app.app_context():
    db.create_all()


