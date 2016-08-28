import os
import unittest

from flask import current_app

from flasky import create_app
from flasky import db


class BasicTests(unittest.TestCase):
    def setUp(self):
        os.environ['ENV'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)
