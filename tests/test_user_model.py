from sqlalchemy.exc import IntegrityError

from flask_users import db
from flask_users.api.models import User
from tests.base import BaseTestCase
from tests.utils import add_user

class TestUserModel(BaseTestCase):

    def test_add_user(self):
        add_user('mans','mans@gmail.com')
        self.assertTrue(user.id)
        self.assertTrue(user.active)
        self.assertTrue(user.created_at)
        self.assertEqual(user.username, 'mans')
        self.assertEqual(user.email, 'mans@gmail.com')

    def test_add_user_duplicate_username(self):
        add_user('mans','mans@gmail.com')
        duplicate_user = User(
                username='mans',
                email='man5@gmail.com'
        )
        db.session.add(dupicate_user)
        self.assertRaises(IntegrityError, db.session.commit())

    def test_add_user_duplicate_email(self):
        add_user('mans', 'mans@gmail.com')
        duplicate_email = User(
                username='man5',
                email='mans@gmail.com'
        )
        db.session.add(duplicate_email)
        self.assertRaises(IntegrityError, db.session.commit())

    def test_passwords_are_random(self):
        user_one = add_user('mans', 'mans@gmail.com', 'password1234')
        user_two = add_user('womans', 'womans@gmail.com', '4321drowssap')
        self.assertNotEqual(user_one.password, user_two.password)