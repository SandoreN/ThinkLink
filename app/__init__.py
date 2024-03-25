import os
from flask import Flask, render_template
from config import Config

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # Initialize Flask extensions here

    # Register blueprints here

    from ...ThinkLink.app import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
    
    @app.route('/')
    def run():
        return render_template("index.html")

    return app