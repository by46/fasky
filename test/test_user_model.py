import unittest

from flasky.models import User


class UserModelTestCase(unittest.TestCase):
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
