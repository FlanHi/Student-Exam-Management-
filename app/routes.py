from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, ResetPasswordRequestForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Exams
from app.forms import LoginForm, RegistrationForm, ExamRecordForm, EditProfileForm, ResetPasswordForm
from werkzeug.urls import url_parse
from datetime import datetime
from app.email import send_password_reset_email

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username. data
        current_user.about_me = form. about_me.data
        db. session. commit ()
        flash ('Your changes have been saved. ')
        return redirect(url_for('profile', username=current_user.username))
    elif request.method == 'GET':
        form. username.data = current_user.username
        form. about_me.data = current_user.about_me
    return render_template(
        'edit_profile.html',
        title='Edit Profile',
        form=form)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@login_required
def index():
    form = ExamRecordForm()
    if form.validate_on_submit():
        exam = Exams(
                subjects=form.subjects.data, 
                term=form.term.data, 
                name=form.name.data, 
                score=form.score.data, 
                year_done=form.year_done.data, 
                year_or_grade=form.year_or_grade.data, 
                author = current_user
                )
        db.session.add(exam)
        db.session.commit()
        flash('Exam recorded')
        return redirect(url_for('index'))
    exams = current_user.exams.order_by(Exams.timestamp.asc()).all()
    print(exams)
    return render_template('index.html', title='Index', form=form, exams=exams)


@app.route('/home/<int:id>', methods=['GET', 'POST'])
def index_exam(id):
    exam = Exams.query.filter_by(id=id).first()
    db.session.delete(exam)
    db.session.commit()
    flash('Deleted Recorded exam')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/<username>/profile')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template(
        'profile.html',
        title="Profile",
        user=user
    )

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user. last_seen = datetime. utcnow()
        db. session.commit ()


@app.route('/request-password-reset', methods=['GET', 'POST'])
def request_password_reset():
    if current_user.is_authenticated:
        return redirect(url_for(index))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash("Check your email for the instructions to reset your password")
        return redirect(url_for('login'))
    return render_template('request_password_reset.html', title='Request Password Reset', form=form)


@app.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template(
        'reset_password.html',
        title='Reset Password',
        form=form
    )