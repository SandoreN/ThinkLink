from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required
from . import *
from app import *
from .models import User
from .views import CRUDView

auth_bp = Blueprint('auth', __name__)
login_manager = LoginManager()
login_manager.init_app(app)

# Create CRUDView instance for User model to interact with the database
user_view = CRUDView(model=User)

@login_manager.user_loader
def load_user(user_id):
    return user_view.get(filters={'id': user_id}, serialized=False)

@auth_bp.route('/register', methods=['POST'])
def register_new_user():
    data = request.get_json()
    if not data or not all([data.get('name'), data.get('username'), data.get('email'), data.get('password')]):
        return jsonify({'message': 'Missing required fields'}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user_data = {
        'name': data['name'],
        'username': data['username'],
        'email': data['email'],
        'password_hash': hashed_password,
        'is_confirmed': True
    }
    
    response, status_code = user_view.post(new_user_data)
    if status_code == 201:
        return jsonify({'message': 'User created successfully.'}), 201

    return response

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = user_view.get({'email': data.get('email')}, serialized=False)
    
    if user and check_password_hash(user.password_hash, data['password']):
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'message': 'Invalid email or password'}), 401

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200