from flask_login import login_required

from flasky.main import main


@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
