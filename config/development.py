import os

# local development environment setting


# WSGI Settings
WSGI_LOG = 'default'

# SQL-Alchemy settings

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.normpath(os.path.join(__file__, '..', '..', 'data.sqlite'))
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
