from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

from flask_users import db
from flask_users.api.models import User
from tests.base import BaseTestCase
from tests.utils import add_user


class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = add_user('mans','mans@gmail.com', 'password1234')
        self.assertTrue(user.id)
        self.assertTrue(user.active)
        self.assertTrue(user.created_at)
        self.assertEqual(user.username, 'mans')
        self.assertEqual(user.email, 'mans@gmail.com')

    def test_add_user_duplicate_username(self):
        add_user('curtis','curtis@gmail.com', 'password1234')
        duplicate_user = User(
                username='curtis',
                email='curtis1@gmail.com',
                password='password1234'
        )
        db.session.add(duplicate_user)
        # self.assertRaises(IntegrityError, db.session.commit())
        with self.assertRaises(IntegrityError) as cm:
            db.session.commit()


    def test_add_user_duplicate_email(self):
        add_user('curtis', 'curtis@gmail.com', 'password1234')
        duplicate_email = User(
                username='man5',
                email='curtis@gmail.com',
                password='password1234'
                )
        db.session.add(duplicate_email)
        # self.assertRaises(IntegrityError, db.session.commit())
        with self.assertRaises(IntegrityError) as cm:
            db.session.commit()

    def test_passwords_are_random(self):
        user_one = add_user('mans', 'mans@gmail.com', 'password1234')
        user_two = add_user('womans', 'womans@gmail.com', '4321drowssap')
        self.assertNotEqual(user_one.password, user_two.password)
    
    def test_encode_auth_token(self):
        user = add_user('mans', 'mans@gmail.com', 'pasword1234')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = add_user('mans', 'mans@gmail.com', '4321drowssap')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertEqual(User.decode_auth_token(auth_token), user.id)