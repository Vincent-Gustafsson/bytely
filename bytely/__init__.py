"""Initializes the flask app"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from bytely.config import Config


db = SQLAlchemy()


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from bytely.models import User, Link
    with app.app_context():
        db.create_all()

    from bytely.users.views import auth
    app.register_blueprint(auth)

    from bytely.main.views import main
    app.register_blueprint(main)

    from bytely.links.views import links
    app.register_blueprint(links)

    return app
