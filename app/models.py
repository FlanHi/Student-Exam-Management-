from datetime import datetime
from app import app, db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))
    exams = db.relationship('Exams', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Exams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.Integer)
    name = db.Column(db.String(64))
    year_done = db.Column(db.String(4))
    year_or_grade = db.Column(db.String(4))
    subjects = db.Column(db.String(64))
    score = db.Column(db.String(4))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Grade: {self.score}'
