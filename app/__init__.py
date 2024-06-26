from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config.from_object(Config)

db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db, render_as_batch=True)
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)
moment = Moment(app)

if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler(
    'logs/tinker_app. log',
    maxBytes=10240,
    backupCount=10)
file_handler. setFormatter(logging. Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging. INFO)
app. logger. addHandler(file_handler)

app. logger.setLevel (logging. INFO)
app. logger. info('Tinker Full-stack App')

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
    if app.config['MAIL_USERNAME' ] or app. config['MAIL_PASSWORD' ]:
        auth = (app. config ['MAIL_USERNAME' ], app.config['MAIL_PASSWORD' ])
    secure = None
    if app.config['MAIL_USE_TLS']:
        secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS' ], subject='Tinker Full-stack Flask App Failure',
            credentials=auth, secure=secure)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

from app import routes, models, errors