from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_cors import CORS

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



db.init_app(app)

from .views import *  # Import the api blueprint
from .models import *

user_view = CRUDView(model=User)

with app.app_context():
    db.create_all()


