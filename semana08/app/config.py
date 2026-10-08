from os import getenv

class Base:
    SQLALCHEMY_TRACK_MODIFICATION = False
    JWT_SECRET_KEY = getenv('JWT_SECRET_KEY')

class Development(Base):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')

class Production(Base):
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')

config_map = {
    "development": Development,
    "production":Production
}