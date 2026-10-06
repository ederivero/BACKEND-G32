from flask import Flask
from flask_restful import Api
from .config import config_map
from .extensions import db, migrate

def create_app(env='development'):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config_map[env])

    db.init_app(app)
    migrate.init_app(app, db)

    return app