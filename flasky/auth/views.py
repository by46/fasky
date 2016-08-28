from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from flasky import db
from flasky.auth import auth
from flasky.models import User
from .forms import LoginForm
from .forms import RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember_me)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash("Invalid User or Password")
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
