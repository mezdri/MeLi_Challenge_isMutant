import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from MutantTest import Model

    app.config.from_mapping(SECRET_KEY='dev')

    basedir = os.path.abspath(os.path.dirname(__file__))
    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    db = SQLAlchemy(app)
    ma = Marshmallow(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app, db, ma
