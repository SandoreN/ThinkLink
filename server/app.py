from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Define the upload folder path relative to the current directory
UPLOAD_FOLDER = 'uploads'
# Configure Flask app to use the specified upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from server.app import routes  # Import routes after initializing Flask app

if __name__ == '__main__':
    app.run(debug=True)