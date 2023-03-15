import logging
from logging.handlers import RotatingFileHandler
import os

import datetime, calendar
from flask import (Flask,
                   url_for,
                   request,
                   render_template,
                   redirect,
                   flash,
                   session
                   )

app = Flask(__name__)


# Standart html Flask vorlage


@app.route('/login', methods=['GET', 'POST'])
def login_site():
    error = None
    if request.method == 'POST':
        if valid_login(request.form["username"], request.form["password"]):
            flash('Succesfully logged in')
            session['username'] = request.form.get("username")
            return redirect(url_for('welcome'))

        else:
            error = "Invalid username or password"
            app.logger.warning('incorrect username or password for user (%s)',
                               request.form.get("username"))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)

    return redirect(url_for('login_site'))


def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


@app.route('/')
def welcome():
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    if 'username' in session:
        app.logger.info('user (%s) logged in ' + time, session['username'])
        return render_template('welcome.html', username=session['username'], time=time)
    else:
        return redirect(url_for('login_site'))


if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.secret_key = os.urandom(24)
    # logging
    handler = RotatingFileHandler('error.log', maxBytes=10240, backupCount=1)
    handler.setLevel(logging.WARNING)
    app.logger.addHandler(handler)
    app.run(host=host, port=port)
