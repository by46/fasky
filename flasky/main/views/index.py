import httplib
import json

from flask import abort
from flask import make_response
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from flask_login import login_required
from flask_wtf import Form
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Required

from flasky import db
from flasky.main import main
from flasky.models import User


class NameForm(Form):
    name = StringField("What's your name", validators=[Required()])
    submit = SubmitField("Submit")


@main.route("/", methods=['GET', 'POST'])
@login_required
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form,
                           name=session.get('name'),
                           known=session.get('known'))


@main.route('/exception/', methods=['GET'])
def exception_with_json():
    message = dict(message='Unkown error')
    response = make_response(json.dumps(message))
    # from flask import  Response
    response.status_code = httplib.INTERNAL_SERVER_ERROR
    response.headers['Content-Type'] = 'Application/json'
    abort(response)


@main.route('/exception2/', methods=['GET'])
def exception_with_handler():
    # abort(httplib.NOT_FOUND)
    return "exception2"
