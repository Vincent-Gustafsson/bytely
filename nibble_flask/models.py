from datetime import datetime
from flask import current_app
from nibble_flask import db, login_manager
from flask_login import UserMixin
from random import choices
import string

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(128))

    links = db.relationship('Link', backref='user', lazy=True)


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_link = db.Column(db.String(512))
    short_link = db.Column(db.String(3), unique=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    times_clicked = db.Column(db.Integer, default=0)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_link = self.generate_short_link()


    def generate_short_link(self):
        characters = string.digits + string.ascii_letters
        # k is how many characters it generates.
        short_link = ''.join(choices(characters, k=3))

        link = self.query.filter_by(short_link=short_link).first()

        if link:
            return self.generate_short_link()
        
        return short_link