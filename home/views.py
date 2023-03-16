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

home_bp = Blueprint('home', __name__)


@home_bp.route('/login', methods=['GET', 'POST'])
def login_site():
    error = None
    if request.method == 'POST':
        if valid_login(request.form["username"], request.form["password"]):
            flash('Succesfully logged in')
            session['username'] = request.form.get("username")
            return redirect(url_for('home.welcome'))

        else:
            error = "Invalid username or password"
            current_app.logger.warning('incorrect username or password for user (%s)',
                                       request.form.get("username"))
    return render_template('home/login.html', error=error)


@home_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home.login_site'))


def valid_login(username, password):
    if username == password:
        return True
    else:
        return False


@home_bp.route('/')
def welcome():
    time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    if 'username' in session:
        current_app.logger.info('user (%s) logged in ' + time, session['username'])
        return render_template('home/welcome.html', username=session['username'], time=time)
    else:
        return redirect(url_for('home.login_site'))
