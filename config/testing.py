# SQL-Alchemy settings
import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.normpath(os.path.join(__file__, '..', '..', 'data_testing.sqlite'))
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
