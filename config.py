# Configuración de la aplicación y leer variables de entorno
"""
from decouple import config


class Config():
    SECRET_KEY = config('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
"""