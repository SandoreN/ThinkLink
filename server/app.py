from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

# Use other configurations from Config class
app.config.from_object(Config)

# Initialize SQLAlchemy database 
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)