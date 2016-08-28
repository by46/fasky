"""flasky

"""
import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

__version__ = '0.0.1'
__author__ = 'benjamin.c.yan'

app = Flask(__name__)

app.config.from_object('config.default')
key = 'ENV'
if key not in os.environ:
    os.environ[key] = 'development'

env = os.environ.get(key)
app.config.from_object('config.{0}'.format(env.lower()))
app.config['VERSION'] = __version__

# Config CORS
CORS(app, resources={'*': {"origins": "*", "methods": "*", "allow-headers": "Content-Type"}})

moment = Moment(app)

Bootstrap(app)

db = SQLAlchemy(app)

from flasky import views
from flasky import models
