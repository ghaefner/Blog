from flask import render_template, request, Blueprint
from flaskblog.models import Post
from calendar import TextCalendar

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    """
    Render the home page with all posts.

    Returns:
        render_template: Home page template with posts.
    """
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    """
    Render the about page.

    Returns:
        render_template: About page template.
    """
    return render_template('about.html', title='About')

@main.route("/calendar")
def calendar():
    """
    Render the clendar page.

    Returns:
        render_template: Calendar page template.
    """
    year = 2024
    month = 2

    cal = TextCalendar(calendar.SUNDAY)
    cal_text = cal.formatmonth(year, month)
    return render_template('calendar.html', calendar_text=cal_text)