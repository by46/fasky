from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager

from flasky import app
from flasky import db

manager = Manager(app)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
