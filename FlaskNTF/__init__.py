import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True )
    app.config.from_object(os.environ.get('APP_SETTINGS'))
    app.config.from_pyfile('settings.cfg', silent=True)

    return app
