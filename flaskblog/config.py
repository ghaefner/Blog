import os

class Config:

    SECRET_KEY = os.environ.get('FLASKBLOG_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # Set email settings for gmail
    MAIL_SERVER = 'mail.gmx.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('GMX_USER')
    MAIL_PASSWORD = os.environ.get('GMX_PASSWORD')