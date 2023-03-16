# Flask NFT-Shop

* Struktur wurde erneuert und auf Flask 2.2.3 sowie python 3.9 angepasst
* Alle Konfigurationsdateien liegen im Ordner conf

### Starten der Anwendung

````
python manage.py runserver
````

### conf/settings.py

Hier können alle Parameter angepasst werden. Nicht jeder Wert wird benötigt
Eine genau Beschreibung der möglichen Parameter sind hier zu finden

[Flask Dokumentation](https://flask.palletsprojects.com/en/2.2.x/config/)
````
import os

# Basisverzeichnis des Projekts
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Pfad zum Templates-Verzeichnis
TEMPLATE_DIR = os.path.join(BASE_DIR, '../templates')
STATIC_DIR = os.path.join(BASE_DIR, '../static')


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False

````

### conf/__init__.py
Initiert die Flask App hier ist nur der teil app = Flask(__name__, .... ) der gegebenenfalls
angepasst werden müsste.

````
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
import sys, os
from .settings import TEMPLATE_DIR, STATIC_DIR, MEDIA_DIR

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../flask_nft')))


def create_app():
    app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR, static_url_path='/media')
    app.config.from_object('conf.settings.Config')

    # logging
    handler = RotatingFileHandler('error.log', maxBytes=10240, backupCount=1)
    handler.setLevel(logging.WARNING)
    app.logger.addHandler(handler)

    # Initialize blueprint
    from home.views import home_bp
    app.register_blueprint(home_bp)

    # Initialize SQLAlchemy for each blueprint
    # example:
    # from home.models import db as home_db
    # home_db.init_app(home_bp)

    return app

````

## Design

Jedes Blueprint hat in den folgenden Ordnern immer ein eigenes Verzeichniss um die übersicht und um die bearbeitung zu vereinfachen. 
Das bedeutet das zum Beispiel der Blueprint home_bp ein verzeichniss im Ordner templates hat

### CSS/IMG/JS

Das alles kann im ordner static im root verzeichniss angepasst werden

### HTML

Alle HTML-Seiten finden sich im Ordner templates 

