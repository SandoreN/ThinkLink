from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from app import *

auth_bp = Blueprint('auth', __name__)

def register_new_user(user_name, username, email_address, password, is_confirmed=False, is_admin=False):
    # Generate password hash
    hashed_password = generate_password_hash(password)
    
    # Create a new user object and add it to the database
    new_user = User(user_name=user_name, username=username, email_address=email_address, password_hash=hashed_password,
                    is_confirmed=is_confirmed, is_admin=is_admin)
    db.session.add(new_user)
    db.session.commit()

    return new_user

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email_address = data['email_address']
    password = data['password']
    
    # Query the database to find the user by email
    user = User.query.filter_by(email_address=email_address).first()
    
    if user and check_password_hash(user.password_hash, password):
        # Authentication successful
        # Here you might generate a JWT token or set a session cookie
        return jsonify({'message': 'Login successful'}), 200
    else:
        # Authentication failed
        return jsonify({'message': 'Invalid email or password'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # Here you might invalidate the JWT token or clear the session cookie
    return jsonify({'message': 'Logout successful'}), 200

# Other authentication-related routes such as forgot password, change password, etc. can be added here

# You might also have routes for user management such as updating user profile, deleting user accounts, etc.