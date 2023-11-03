from datetime import datetime
from app import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'User {self.username}'

class Exams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Term = db.Column(db.Integer, primary_key=True)
    School = db.Column(db.String(64))
    Math = db.Column(db.Integer, primary_key=True)
    English = db.Column(db.Integer, primary_key=True)
    Comment = db.Column(db.Text, primary_key=True)
    
