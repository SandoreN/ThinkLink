import os

# Define the base directory of the project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Flask app configuration
class Config:
    """
    Configuration class for the application.

    Attributes:
        SECRET_KEY (str): Secret key for secure session management.
        SECURITY_PASSWORD_SALT (str): Salt for password hashing.
        SQLALCHEMY_DATABASE_URI (str): URI for the database connection.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to enable/disable modification tracking.
        FLASK_APP_FS_ROOT (str): Root folder for file system configuration.
        MAIL_SERVER (str): SMTP server for sending emails.
        MAIL_PORT (int): Port number for the mail server.
        MAIL_USE_SSL (bool): Flag to enable/disable SSL for email communication.
        MAIL_USERNAME (str): Username for the email account.
        MAIL_PASSWORD (str): Password for the email account.
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key_here'
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False
    FLASK_APP_FS_ROOT = os.environ.get('FLASK_APP_FS_ROOT') or 'your_upload_folder_here'
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 465
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_SAMESITE = 'Lax'
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