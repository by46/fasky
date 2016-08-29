from flasky import login_manager
from .permission import Permission
from .role import Role
from .user import AnonymousUser
from .user import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
