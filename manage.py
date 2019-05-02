import unittest
import coverage

from flask_script import Manager
from flask_migrate import MigrateCommand

from flask_users import create_app, db
from flask_users.api.models import User


app = create_app()
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.command
def recreate_db():
    """
    Recreate database
    """
    db.drop_all()
    db.create_all()
    db.session.commit()

@manager.command
def test():
    """
    Run tests without code coverage
    """
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def seed_db():
    """
    Seed the database
    """
    db.session.add(User(username='mans', email='mans@gmail.com'))
    db.session.add(User(username='wayua', email='wayua@gmail.com'))
    db.session.commit()

COV = coverage.coverage(
    branch=True,
    include='flask_users/*',
    omit=[
        'flask_users/tests/*',
        'flask_users/server/config.py',
        'flask_users/server/*/__init__.py'
    ]
)

COV.start()

@manager.command
def cov():
    """
    Run unit tests withc coverage
    """
    tests = unittest.TestLoader().discover('./tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage summary')
        COV.report()
        COV.erase()
        return 0
    return 1


if __name__ == '__main__':
    manager.run()