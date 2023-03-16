from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    is_author = db.Column(db.Boolean, default=False)

    def __init__(self, fullname, username, email, password, is_author=False):
        self.fullname = fullname
        self.username = username
        self.email = email
        self.password = password
        self.is_author = is_author

    def __repr__(self):
        return '<Author %r>' % self.username
