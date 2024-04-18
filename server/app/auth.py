from flask import Blueprint, jsonify, request
from flask_login import LoginManager, login_user, logout_user, login_required
from app import app
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
    """
    Register a new user.

    This function handles the registration of a new user by receiving a POST request with the user's information.
    The required fields are 'name', 'username', 'email', and 'password'. If any of these fields are missing, a
    response with a status code of 400 and a message indicating the missing fields is returned.

    If all the required fields are provided, the password is stored as plain text for simplicity in this example.
    A new_user_data dictionary is created with the user's information. The 'is_confirmed' field is set to True
    indicating that the user's account is confirmed.

    The new_user_data is then passed to the user_view.post function to create a new user. If the user is created
    successfully, a response with a status code of 201 and a message indicating the successful creation is returned.
    Otherwise, the response returned by user_view.post is returned.

    Returns:
        A JSON response with a status code and a message indicating the result of the registration process.
    """
    data = request.get_json()
    if not data or not all([data.get('name'), data.get('username'), data.get('email'), data.get('password_hash')]):
        return jsonify({'message': 'Missing required fields'}), 400

    new_user_data = {
        'name': data['name'],
        'username': data['username'],
        'email': data['email'],
        'password_hash': data['password_hash'],  # Store password as plain text
        'is_confirmed': True
    }
    
    response, status_code = user_view.post(new_user_data)
    if status_code == 201:
        return jsonify({'message': 'User created successfully.'}), 201

    return response

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user by checking their email and password.

    Returns:
        A JSON response indicating the result of the login attempt.
    """
    data = request.get_json()
    user = user_view.get({'email': data.get('email')}, serialized=False)
    
    if user and user.password == data['password']:  # Direct comparison without hashing
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'message': 'Invalid email or password'}), 401

@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    """
    Logout the currently logged-in user.

    Returns:
        A JSON response with a success message and HTTP status code 200.
    """
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200
