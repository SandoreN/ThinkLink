import os

# Define the base directory of the project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Flask app configuration
class Config:
    # Secret key for secure session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False

    #File System configuration
    APP_FS_ROOT = os.environ.get('UPLOAD_FOLDER') or 'your_upload_folder_here'

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 465
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# Development configuration
class DevelopmentConfig(Config):
    DEBUG = True

# Production configuration
class ProductionConfig(Config):
    DEBUG = False

# Add more configurations as needed

# Configurations by environment
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    # Add more environments if needed
}