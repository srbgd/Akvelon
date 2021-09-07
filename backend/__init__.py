"""
This module is used to initialize some singletons needed for the application
"""


from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
from os import environ


db = SQLAlchemy()
ma = Marshmallow()
flask_app = None


def get_flask_app():
    """
    Initialize flask application if it haven't been initialized yet

    :return: flask application instance
    """
    global flask_app
    if flask_app is None:
        flask_app = Flask(__name__)
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = \
            f"postgresql://flask_orm:qwerty@{environ.get('DB_HOST', 'localhost')}:5432/flask_db"
        flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(flask_app)
        db.create_all(app=flask_app)
    return flask_app
