from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bootstrap.init_app(app)

    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.main.views import page_not_found, internal_error
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_error)

    return app
