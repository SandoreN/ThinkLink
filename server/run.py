from app import app
from app.auth import auth_bp

app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run()