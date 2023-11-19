from app import app, db
from flask import render_template, flash, redirect, url_for, request
#from app.forms import LoginForm, ProForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Exams
from app.forms import LoginForm, RegistrationForm, ExamRecordForm
from werkzeug.urls import url_parse


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
