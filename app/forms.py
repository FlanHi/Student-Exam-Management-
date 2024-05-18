from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Email, EqualTo
from app.models import User

class EditProfileForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 16)])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Edit profile')


class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 16)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    """Registration Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 16)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Login')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class ExamRecordForm(FlaskForm):
    """Exam Record Form"""
    term = SelectField(
        'Term',
        choices=[
            (1, 1),
            (2, 2),
            (3, 3)
        ],
        validators=[DataRequired(), Length(1, 16)])
    year_done = StringField('Year done', validators=[DataRequired()])
    subjects = StringField('Student\'s subject', validators=[DataRequired()])
    score = StringField('Score (%)', validators=[DataRequired()])
    year_or_grade = StringField('Student\'s Year or Grade', validators=[DataRequired()])
    name = StringField('Student\'s name', validators=[DataRequired()])
    submit = SubmitField('Save')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField("Request Password Reset")

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField(
        'Confirm password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Reset Password')