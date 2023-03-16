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

block_bp = Blueprint('block', __name__)


@block_bp.route('/')
def block():
    return '<h1>Block Blueprint TEST</h1>'