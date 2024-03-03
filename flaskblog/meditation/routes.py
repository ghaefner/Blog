from flask import render_template, Blueprint

meditation = Blueprint('meditation', __name__, template_folder='templates')

@meditation.route("/meditation/videos")
def videos():
    return render_template('meditation_video.html', title='Meditation Videos')

@meditation.route("/meditation/exercise")
def excercise():
    return render_template('mindful_exercise.html', title='Mindfulness Exercise')