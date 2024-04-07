import os

# Define the base directory of the project
#BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Flask app configuration
class Config:
    # Secret key for secure session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #File System configuration
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or 'your_upload_folder_here'

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