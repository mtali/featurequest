import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

# create flask app, set the configuration in environment variables
app = create_app(os.getenv('FEATUREQUEST_CONFIG') or 'default')
manager = Manager(app)
migrare = Migrate(app, db)

def make_shell_context():
    """Pre-populate shell"""
    return dict(app=app,db=db)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
