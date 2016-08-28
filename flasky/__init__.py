"""flasky

"""
import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

__version__ = '0.0.1'
__author__ = 'benjamin.c.yan'

moment = Moment()
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.default')
    key = 'ENV'
    if key not in os.environ:
        os.environ[key] = 'development'

    env = os.environ.get(key)
    app.config.from_object('config.{0}'.format(env.lower()))
    app.config['VERSION'] = __version__

    moment.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    return app
