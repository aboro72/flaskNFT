from flask import current_app
from datetime import datetime
from flask import (Blueprint,
                   url_for,
                   request,
                   render_template,
                   redirect,
                   flash,
                   session
                   )

author_bp = Blueprint('author', __name__)


@author_bp.route('/')
def block():
    return '<h1>Author Blueprint TEST</h1>'