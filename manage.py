from app import create_app,db
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Pitch,Comment,Upvotes,Downvotes

from flask_script import Manager,Server


# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)


migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Comment=Comment, Upvotes=Upvotes, Downvotes=Downvotes)

if __name__ == '__main__':
    manager.run()
