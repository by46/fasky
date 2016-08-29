from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_script import Shell

from flasky import create_app
from flasky import db
from flasky.models import Role
from flasky.models import User

app = create_app('development')
manager = Manager(app)

migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
