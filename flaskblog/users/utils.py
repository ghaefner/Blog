import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import mail, app

def save_picture(form_picture):
    """
    Save the profile picture uploaded by the user.

    Args:
        form_picture: Uploaded picture file.

    Returns:
        str: Filename of the saved picture.
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn



def send_reset_email(user):
    """" Send email with the reset token generated for the user."""
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender=app.config['MAIL_USERNAME'], 
                  recipients=[user.email])
    msg.body = f'''Dear {user.username}

To reset your password, visit the following link:

{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will happen.
You might want to check your account information if you did not make this request. 
Always be aware about sharing your personal account information with others.

Best regards,
Your Blog-Team
'''
    mail.send(msg)