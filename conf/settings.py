import os

# Basisverzeichnis des Projekts
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Pfad zum Templates-Verzeichnis
TEMPLATE_DIR = os.path.join(BASE_DIR, '../templates')
STATIC_DIR = os.path.join(BASE_DIR, '../static')
MEDIA_DIR = os.path.join(BASE_DIR, '../media')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
