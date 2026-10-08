from flask import Flask
from flask_restful import Api
from .config import config_map
from .extensions import db, migrate
from .models import *
from .api import RegistroController, LoginController

def create_app(env='development'):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config_map[env])

    db.init_app(app)
    migrate.init_app(app, db)

    api.add_resource(RegistroController, '/registro')
    api.add_resource(LoginController, '/login')
    
    return app