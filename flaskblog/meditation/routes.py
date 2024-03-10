from flask import render_template, Blueprint

meditation = Blueprint('meditation', __name__, template_folder='templates')

@meditation.route("/meditation/videos")
def videos():
    return render_template('meditation_video.html', title='Meditation Videos')

@meditation.route("/meditation/exercise")
def exercise():
    return render_template('mindful_exercise.html', title='Mindfulness Exercise')

@meditation.route('/mindful_question', methods=['GET', 'POST'])
def mindful_question():
    # form = MindfulQuestionForm()
    # if form.validate_on_submit():
        # Process form data here
        # For example, you can save the submitted data to the database
        # Or perform any other actions based on the user's input
        # Redirect the user to a new page or display a success message
    return render_template('mindful_question.html', title='Mindfulness Questionnaire') # form=form)