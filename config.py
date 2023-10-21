import os

class Config(object):
    """Define app configurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'