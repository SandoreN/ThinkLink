from flask import Blueprint, jsonify, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
import jwt
from datetime import datetime, timedelta
from functools import wraps
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from . import *
from app import *
from .models import User, Token
from .views import CRUDView

auth_bp = Blueprint('auth', __name__)

# Create CRUDView instances for User and Token models to interact with the database
user_view = CRUDView(model=User)
token_view = CRUDView(model=Token)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token_str = request.headers.get('Authorization', '').split(' ')[1] if 'Authorization' in request.headers else None
        if not token_str:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token_str, app.config['SECRET_KEY'], algorithms=['HS256'])
            if 'user_id' in data:
                token = token_view.get(filters={'token': token_str}, serialized=False)
                if not token or token.is_blacklisted:
                    return jsonify({'message': 'Token is invalid or has been blacklisted'}), 401
                user = user_view.get(filters={'id': data['user_id']}, serialized=False)
                if not user:
                    return jsonify({'message': 'User not found'}), 401
            else:
                return jsonify({'message': 'Invalid token'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        # changed from f(token, *args, **kwargs) to f(user, *args, **kwargs) as the /protected route expects a user. 
        return f(user, *args, **kwargs)
    return decorated


@auth_bp.route('/register', methods=['POST'])
def register_new_user():
    data = request.get_json()
    if not data or not all([data.get('name'), data.get('username'), data.get('email'), data.get('password')]):
        return jsonify({'message': 'Missing required fields'}), 400


    # Check if email already exists
    if user_view.get(filters={"email": data['email']}).first():
        return jsonify({'message': 'Username already exists'}), 400

    # Check if username already exists
    if user_view.get(filters={"username": data['username']}).first():
        return jsonify({'message': 'Email already exists'}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user_data = {
        'name': data['name'],
        'username': data['username'],
        'email': data['email'],
        'password_hash': hashed_password,
        'is_confirmed': False
    }
    
    response, status_code = user_view.post(new_user_data)
    if status_code == 201:
        send_confirmation_email(data['email'], generate_confirmation_token(data['email']))
        return jsonify({'message': 'User created successfully. Please check your email to confirm it.'}), 201

    return response

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = user_view.get({'email': data.get('email')}, serialized=False)
    
    if user and check_password_hash(user.password_hash, data['password']):
        token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token, 'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid email or password'}), 401

@auth_bp.route('/logout', methods=['POST'])
@token_required
def logout(current_user):
    token_str = request.headers['Authorization'].split(' ')[1]
    token = token_view.get(filters={'token': token_str}, serialized=False)
    if token:
        token_view.put(token.id, {'is_blacklisted': True})
        return jsonify({'message': 'Logout successful'}), 200
    return jsonify({'message': 'Token not found'}), 404

@auth_bp.route('/protected', methods=['GET'])
@token_required
def protected(current_user):
    return jsonify({'message': 'Access granted', 'user': current_user.serialize()}), 200

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

def send_confirmation_email(email, token):
    confirm_url = url_for('.confirm_email', token=token, _external=True)
    message = MIMEMultipart()
    message['From'] = app.config['MAIL_USERNAME']
    message['To'] = email
    message['Subject'] = 'Confirm Your Email Address'
    html_content = f"<p>Please click <a href='{confirm_url}'>here</a> to confirm your email address.</p>"
    message.attach(MIMEText(html_content, 'html'))
    with smtplib.SMTP_SSL(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
        server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        server.send_message(message)