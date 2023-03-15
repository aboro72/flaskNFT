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
                   make_response,
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

# ----------------------------------------------------------------
#
# def hello():
#   return render_template('hello.html')


# Standart Flask Vorlagen
'''
@app.route('/')
def index():
    return 'Leere Seite'


@app.route('/username/<username>')
def show_user_profile(username):
    # show the user profile
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post
    return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login_site():
    if request.method == 'POST':
        return 'username is: ' + request.values["username"]
    else:
        return '<form action="/login" method="post"><input type=t"ext" name="username"/><p><button type="submit">Submit</button>'



@app.route('/hello_time')
def hello_world():  # put application's code here
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return '<h1>' + 'Hello World! it is: ' + time + '</h1> </br>'
'''

if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.secret_key = os.urandom(24)
    # logging
    handler = RotatingFileHandler('site.log', maxBytes=10240, backupCount=1)
    handler.setLevel(logging.WARNING)
    app.logger.addHandler(handler)
    app.run(host=host, port=port)
