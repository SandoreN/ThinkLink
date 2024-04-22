from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_cors import CORS
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

app = Flask(__name__)
CORS(app, origins=['http://localhost:8080'], supports_credentials=True)

from flask import session

@app.before_request
def make_session_permanent():
    session.permanent = True
    
from app.auth import auth_bp
from app.routes import routes_bp
app.register_blueprint(auth_bp)
app.register_blueprint(routes_bp)

# Use other configurations from Config class
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)

from .views import *  # Import the api blueprint
from .models import *

user_view = CRUDView(model=User)

@login_manager.user_loader
def load_user(user_id):
    user, status = user_view.get(filters={'id': user_id}, serialized=False)
    current_app.logger.info(f"Loaded user {user.id}")
    return user

with app.app_context():
    db.create_all()


