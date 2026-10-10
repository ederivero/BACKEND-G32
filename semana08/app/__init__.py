from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .config import config_map
from .extensions import db, migrate
from .models import *
from .api import RegistroController, LoginController, UsuarioController, ChangePasswordController, ResetPasswordController

def create_app(env='development'):
    app = Flask(__name__)
    api = Api(app)
    # Aca inicializamos la instancia de JWT para que pueda ser utilizada entodo el proyecto
    JWTManager(app)
    app.config.from_object(config_map[env])

    db.init_app(app)
    migrate.init_app(app, db)

    api.add_resource(RegistroController, '/registro')
    api.add_resource(LoginController, '/login')
    api.add_resource(UsuarioController, '/usuario')
    api.add_resource(ChangePasswordController, '/change-password')
    api.add_resource(ResetPasswordController,'/reset-password')


    return app