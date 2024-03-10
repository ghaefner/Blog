from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class MindfulQuestionForm(FlaskForm):
    question1 = TextAreaField('Question 1', validators=[DataRequired()])
    question2 = TextAreaField('Question 2', validators=[DataRequired()])
    # Add more TextAreaField for additional questions
    submit = SubmitField('Submit')
