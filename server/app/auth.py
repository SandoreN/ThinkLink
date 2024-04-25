from flask import Blueprint, jsonify, request, session
from . import *
from app import *
from .models import User
from .views import CRUDView

auth_bp = Blueprint('auth', __name__)

# Create CRUDView instance for User model to interact with the database
user_view = CRUDView(model=User)

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
    if not data or not all([data['name'], data['username'], data['email'], data['password']]):
        return jsonify({'message': 'Missing required fields'}), 400

    new_user_data = {
        'name': data['name'],
        'username': data['username'],
        'email': data['email'],
        'password': data['password'],
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
    user, status = user_view.get(filters={'email': data['email']}, serialized=False)
    
    if user and user.password == data['password']:  # Direct comparison without hashing
        
        user_dict = {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'name': user.name
        }
        session['user'] = user_dict
        return jsonify({'message': 'Logged in successfully.', 'user': user_dict}), 200
    return 'Invalid username or password'

@auth_bp.route('/logout')
def logout():
    """
    Logout the currently logged-in user.

    Returns:
        A JSON response with a success message and HTTP status code 200.
    """
    session.pop('user', None)
    return jsonify({'message': 'Logged out successfully.'}), 200