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
    from block.views import block_bp
    app.register_blueprint(block_bp, url_prefix='/block')
    from author.views import author_bp
    app.register_blueprint(author_bp, url_prefix='/author')
    # Initialize SQLAlchemy for each blueprint
    # example:
    # from home.models import db as home_db
    # home_db.init_app(home_bp)
    from author.models import db as author_db
    author_db.init_app(author_bp)

    return app
