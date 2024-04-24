from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

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

# Assuming that views and models modules don't cause circular imports
from .views import *
from .models import *

user_view = CRUDView(model=User)

with app.app_context():
    db.create_all()


