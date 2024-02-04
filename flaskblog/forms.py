"""
forms.py - Defines forms used in the Flask Blog application.

This module defines various FlaskForm classes using Flask-WTF and WTForms for user registration,
login, updating account information, and creating posts.

Classes:
    - RegistrationForm: Form for user registration.
    - LoginForm: Form for user login.
    - UpdateAccountForm: Form for updating user account information and profile picture.
    - PostForm: Form for creating new blog posts.
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    """
    RegistrationForm class - Form for user registration.

    Attributes:
        username: StringField for user's desired username.
        email: StringField for user's email.
        password: PasswordField for user's password.
        confirm_password: PasswordField to confirm user's password.
        submit: SubmitField to submit the registration form.

    Methods:
        validate_username: Validates the uniqueness of the entered username.
        validate_email: Validates the uniqueness of the entered email.
    """

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Validates the uniqueness of the entered username."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """Validates the uniqueness of the entered email."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    """
    LoginForm class - Form for user login.

    Attributes:
        email: StringField for user's email.
        password: PasswordField for user's password.
        remember: BooleanField to remember user's login state.
        submit: SubmitField to submit the login form.
    """

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    """
    UpdateAccountForm class - Form for updating user account information and profile picture.

    Attributes:
        username: StringField for user's desired username.
        email: StringField for user's email.
        picture: FileField for updating user's profile picture.
        submit: SubmitField to submit the update form.
        delete_picture: SubmitField to delete user's profile picture.

    Methods:
        validate_username: Validates the uniqueness of the entered username.
        validate_email: Validates the uniqueness of the entered email.
    """

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')
    delete_picture = SubmitField('Delete Profile Picture')

    def validate_username(self, username):
        """Validates the uniqueness of the entered username."""
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """Validates the uniqueness of the entered email."""
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    """
    PostForm class - Form for creating new blog posts.

    Attributes:
        title: StringField for post title.
        content: TextAreaField for post content.
        submit: SubmitField to submit the post form.
    """

    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
