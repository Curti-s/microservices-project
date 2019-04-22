import unittest

from flask_script import Manager

from flask_users import create_app, db
from flask_users.api.models import User


app = create_app()
manager = Manager(app)

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


if __name__ == '__main__':
    manager.run()