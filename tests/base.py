from flask_testing import TestCase

from flask_users import app, db


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('flask_users.config.TestingConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

