import httplib

from flask import abort
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask_login import current_user
from flask_login import login_required

from flasky import db
from flasky.decorators import admin_required
from flasky.main import main
from flasky.main.forms import EditProfileAdminForm
from flasky.main.forms import EdtProfileForm
from flasky.models import Role
from flasky.models import User


@main.route('/user/<username>')
def user(username):
    u = User.query.filter_by(username=username).first()
    if u is None:
        abort(httplib.NOT_FOUND)

    return render_template('user.html', user=u)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EdtProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        return redirect(url_for('main.user', username=current_user.username))

    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(user_id):
    u = User.query.get_or_404(user_id)
    form = EditProfileAdminForm(user=u)
    if form.validate_on_submit():
        u.name = form.name.data
        u.username = form.username.data
        u.email = form.email.data
        u.confirmed = form.confirmed.data
        u.role = Role.query.get(form.role.data)
        u.location = form.location.data
        u.about_me = form.about_me.data
        db.session.add(u)
        flash('The profile has been updated.')
        return redirect(url_for('main.user', username=u.username))

    form.name.data = u.name
    form.username.data = u.username
    form.email.data = u.email
    form.confirmed.data = u.confirmed
    form.role.data = u.role_id
    form.location.data = u.location
    form.about_me.data = u.about_me
    return render_template('edit_profile.html', form=form)
