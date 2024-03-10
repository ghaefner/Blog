import json
import logging

from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.validators import DataRequired

class MindfulQuestionForm(FlaskForm):
    def __init__(self, questions_file, *args, **kwargs):
        super(MindfulQuestionForm, self).__init__(*args, **kwargs)
        self.load_questions(questions_file)

    def load_questions(self, questions_file):
        try:
            with open(questions_file, 'r') as file:
                questions_data = json.load(file)

            for i, question in enumerate(questions_data, start=1):
                field_name = f"question_{i}"
                options = [(index, option) for index, option in enumerate(question['options'], start=1)]
                setattr(self, field_name, SelectField(question['question'], choices=options, validators=[DataRequired()]))
        except Exception as e:
            logging.error(f"Error loading questions from {questions_file}: {e}")
