import unittest

from flasky import create_app
from flasky import db
from flasky.models import AnonymousUser
from flasky.models import Permission
from flasky.models import Role
from flasky.models import User


class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_setter(self):
        user = User(password='cat')
        self.assertFalse(user.password_hash is None)

    def test_no_password_getter(self):
        user = User(password='cat')
        with self.assertRaises(AttributeError):
            user.password

    def test_verify_password(self):
        user = User(password='cat')
        self.assertTrue(user.verify_password('cat'))
        self.assertFalse(user.verify_password('dog'))

    def test_password_salt_are_random(self):
        u1 = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u1.password_hash != u2.password_hash)

    def test_roles_and_permissions(self):
        Role.insert_roles()
        user = User(email='john@example.com', password='cat')
        self.assertTrue(user.can(Permission.WRITE_ARTICLES))
        self.assertFalse(user.can(Permission.MODERATE_COMMENTS))

        admin = User(email='ycs_ctbu_2010@126.com')
        self.assertTrue(admin.can(Permission.FOLLOW))
        self.assertTrue(admin.can(Permission.COMMENT))
        self.assertTrue(admin.can(Permission.MODERATE_COMMENTS))
        self.assertTrue(admin.can(Permission.WRITE_ARTICLES))
        self.assertTrue(admin.can(Permission.ADMINISTER))
        self.assertTrue(admin.is_administrator())



    def test_anonymous_permission(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
        self.assertFalse(u.can(Permission.COMMENT))
        self.assertFalse(u.can(Permission.MODERATE_COMMENTS))
        self.assertFalse(u.can(Permission.WRITE_ARTICLES))
        self.assertFalse(u.can(Permission.ADMINISTER))
