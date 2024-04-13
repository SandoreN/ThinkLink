import smtplib
from flask import Blueprint, jsonify, request, url_for, render_template
from . import config
from . import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from itsdangerous import URLSafeTimedSerializer
from sqlalchemy.exc import IntegrityError
import jwt

auth_bp = Blueprint('auth', __name__)

# Instantiate CRUDView for User model
user_view = CRUDView()
user_view.model = User

@auth_bp.route('/register', methods=['POST'])
def register_new_user():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No JSON data received'}), 400
    
    # Extract required fields from JSON data
    name = data.get('name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if required fields are missing
    if not (name and email and password and username):
        return jsonify({'message': 'Username, email, or password field is missing'}), 400

    # Generate password hash
    password_hash = generate_password_hash(password_hash)

    # Create a new user instance data
    new_user_data = {'name': name, 'email': email, 'password_hash': password_hash}

    request.json = new_user_data
    # Use CRUDView to create the new user
    try:
        response = user_view.post()
    except IntegrityError:
        return jsonify({'message': 'Username or email already exists. Please try again.'}), 400

    confirmation_token = generate_confirmation_token(email)

    send_confirmation_email(email, confirmation_token)

    return response

@auth_bp.route('/confirm_email/<token>', methods=['GET'])
def confirm_email(token):
    email = verify_confirmation_token(token)
    if email:
        # This is how you would filter by any particular "column_name": "value"
        # Prepare the request.json to filter by email
        request.json = {'email': email}
        # Send a GET request to the /api/users endpoint
        user = user_view.get()
        if user:
            # prepare a PATCH request to update the user's is_confirmed field
            request.json = {'is_confirmed': True}
            # send the PATCH request
            user_view.patch(user['id'])
            return jsonify({'message': 'Email confirmed successfully.'}), 200
    return jsonify({'error': 'Invalid token or email not found.'}), 400


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    # Query the database to find the user by email
    request.json = {'email': email}
    user = user_view.get(serialized=False)
    
    if user and check_password_hash(user.password_hash, password):
        # Authentication successful
        # Here you might generate a JWT token or set a session cookie
        token = jwt.encode({'email': user.email}, 'secret', algorithm='HS256')

        return jsonify({'message': 'Login successful'}), 200
    else:
        # Authentication failed
        return jsonify({'message': 'Invalid email or password'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    # Here you might invalidate the JWT token or clear the session cookie
    return jsonify({'message': 'Logout successful'}), 200

# Other authentication-related routes such as forgot password, change password, etc. can be added here

def generate_confirmation_token(email):
    return generate_password_hash(email)

def send_confirmation_email(email, confirmation_token):
    confirm_url = url_for('auth.confirm_email', token=confirmation_token, _external=True)

    # Create the email message
    message = MIMEMultipart()
    message['From'] = app.config['MAIL_USERNAME']
    message['To'] = email
    message['Subject'] = 'Confirm Your Email Address'

    # HTML content for the email
    html_content = f"<p>Please click <a href='{confirm_url}'>here</a> to confirm your email address.</p>"

    # Attach HTML content to the email
    message.attach(MIMEText(html_content, 'html'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
        server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        server.send_message(message)






def verify_confirmation_token(token):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'], max_age=3600)
        return email
    except:
        return None
# You might also have routes for user management such as updating user profile, deleting user accounts, etc.