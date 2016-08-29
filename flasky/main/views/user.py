import httplib

from flask import abort
from flask import render_template

from flasky.main import main
from flasky.models import User


@main.route('/user/<username>')
def user(username):
    u = User.query.filter_by(username=username).first()
    if u is None:
        abort(httplib.NOT_FOUND)

    return render_template('user.html', user=u)
