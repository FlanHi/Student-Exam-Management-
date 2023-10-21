from app import app
from flask import render_template, flash, redirect, url_for
#from app.forms import LoginForm, ProForm

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Index')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')