from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Aca inicializamos el uso de el ORM
db = SQLAlchemy()

# Aca inicializamos el uso del administrador de migraciones de la bd
migrate = Migrate()