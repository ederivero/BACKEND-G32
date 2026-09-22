from flask import Flask
from .config import config_map
from .extensions import db, migrate

# Al usar el patron de diseño Application Factory se recomienda crear una funcion llamada create_app en la cual se inicializara todo el proyecto y asi mismo puede recibir parametros para los diferentes entornos de prueba
def create_app(env = "development"):
    app = Flask(__name__)
    # from_object > actualiza los valores que le pasemos en el parametro para que la instancia de Flask arranque con esas modificaciones de sus parametros, por ejemplo Debug, entre otros
    app.config.from_object(config_map[env])

    # Inicializamos la instancia de la base de datos pasandole la instancia de Flask para que utilice las variables que hemos configurado en la instancia (config_map)
    db.init_app(app)

    # Inicializamos la instancia de las migraciones para ahora declara nuestra configuracion de la instancia de flask y nuestra configuracion de la base de datos
    migrate.init_app(app, db)


    return app