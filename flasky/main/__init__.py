from flask import Blueprint

from flasky.models import Permission

main = Blueprint('main', __name__, url_prefix='/main')

from . import views


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
