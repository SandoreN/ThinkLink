from flask import Blueprint, jsonify, request, url_for, render_template
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
from .models import User, BlacklistedToken
from .views import CRUDView
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint('auth', __name__)

# Initialize CRUDView with the User model
user_view = CRUDView(model=User)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').split(' ')[1] if 'Authorization' in request.headers else None
        if not token or BlacklistedToken.query.filter_by(token=token).first():
            return jsonify({'message': 'Token is missing or has been blacklisted'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            if 'user_id' in data:
                current_user = User.query.get(data['user_id'])
                if not current_user:
                    return jsonify({'message': 'User not found'}), 404
            else:
                return jsonify({'message': 'Invalid token'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        return f(current_user, *args, **kwargs)
    return decorated


@auth_bp.route('/api/register', methods=['POST'])
def register_new_user():
    data = request.get_json()
    if not data or not all([data.get('name'), data.get('username'), data.get('email'), data.get('password')]):
        return jsonify({'message': 'Missing required fields'}), 400

    if user_view.get(None, serialized=False):
        return jsonify({'message': 'Username or email already exists'}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user_data = {
        'name': data['name'],
        'username': data['username'],
        'email': data['email'],
        'password_hash': hashed_password,
        'is_confirmed': False
    }

    try:
        response, status_code = user_view.post(new_user_data)
        if status_code == 201:
            send_confirmation_email(data['email'], generate_confirmation_token(data['email']))
            return jsonify({'message': 'User created successfully. Please check your email to confirm it.'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Username or email already exists'}), 400

    return jsonify({'message': 'Failed to create user'}), 400

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = user_view.get({'email': data.get('email')}, serialized=False)
    
    if user and check_password_hash(user.password_hash, data['password']):
        token = jwt.encode({'user_id': user.id, 'exp': datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token, 'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid email or password'}), 401

@auth_bp.route('/api/logout', methods=['POST'])
@token_required
def logout(current_user):
    token = request.headers['Authorization'].split(' ')[1]
    blacklist_token = BlacklistedToken(token=token)
    db.session.add(blacklist_token)
    db.session.commit()
    return jsonify({'message': 'Logout successful'}), 200

@auth_bp.route('/api/protected', methods=['GET'])
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

