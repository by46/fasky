from flask_login import login_required

from flasky.decorators import admin_required
from flasky.decorators import permission_required
from flasky.main import main
from flasky.models import Permission


@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'


@main.route('/admin', endpoint='administrator')
@login_required
@admin_required
def for_admin_only():
    return "only for administrator!"


@main.route('/moderator', endpoint='moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "For comment moderators!"
