import os
import datetime, calendar
from flask import Flask,url_for

app = Flask(__name__)


@app.route('/')
def index():
    return url_for('show_user_profile', username='Andreas')


@app.route('/username/<username>')
def show_user_profile(username):
    # show the user profile
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post
    return 'Post %d' % post_id


@app.route('/hello_time')
def hello_world():  # put application's code here
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return '<h1>' + 'Hello World! it is: ' + time + '</h1> </br>'


if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host=host, port=port)
