import os

import datetime, calendar
from flask import Flask, url_for, request, render_template, redirect, flash

app = Flask(__name__)

# Standart html Flask vorlage


@app.route('/')
def index():
    return 'Leere Seite'


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return render_template('hello1.html', name_template=name, time=time)


@app.route('/login', methods=['GET', 'POST'])
def login_site():
    error = None
    if request.method == 'POST':
        if valid_login(request.form["username"], request.form["password"]):
            flash('You were logged in')
            return redirect(url_for('welcome', username=request.form.get("username")))
        else:
            error = "Invalid username or password"

    return render_template('login.html', error=error)


def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


@app.route('/welcome/<username>')
def welcome(username):
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return render_template('welcome.html', username=username, time=time)


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
    app.run(host=host, port=port)
