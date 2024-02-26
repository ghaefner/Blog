from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

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