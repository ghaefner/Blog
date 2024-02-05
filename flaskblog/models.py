"""
models.py - Defines database models for the Flask Blog application.

This module defines SQLAlchemy models for User and Post, which represent the users and blog posts in the application.

Classes:
    - User: Represents a user in the application.
    - Post: Represents a blog post in the application.
"""

from datetime import datetime
from flaskblog import db, login_manager
from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    """Loads a user by their user ID."""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    User class - Represents a user in the application.

    Attributes:
        id: IntegerField for user's unique ID.
        username: StringField for user's username.
        email: StringField for user's email.
        image_file: StringField for user's profile picture filename.
        password: StringField for user's hashed password.
        posts: Relationship to Post objects authored by the user.

    Methods:
        __repr__: Returns a string representation of the User object.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        """Returns a token to reset password that expires in 30mins."""
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        """ Verifys reset token. Trys to get the user ID from the token and returns that user."""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
    
    def __repr__(self):
        """Returns a string representation of the User object."""
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    """
    Post class - Represents a blog post in the application.

    Attributes:
        id: IntegerField for post's unique ID.
        title: StringField for post's title.
        date_posted: DateTimeField for post's date of creation.
        content: TextField for post's content.
        user_id: ForeignKey to the User object who authored the post.

    Methods:
        __repr__: Returns a string representation of the Post object.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """Returns a string representation of the Post object."""
        return f"Post('{self.title}', '{self.date_posted}')"
