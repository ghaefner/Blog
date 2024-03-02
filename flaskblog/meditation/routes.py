from flask import render_template, Blueprint

meditation = Blueprint('meditation', __name__, template_folder='templates')

@meditation.route("/meditation/videos")
def videos():
    return render_template('meditation_video.html', title='Meditation Videos')
