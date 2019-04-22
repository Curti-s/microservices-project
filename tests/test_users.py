import json

from tests.base import BaseTestCase
from flask_users import db
from flask_users.api.models import User


def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user
class TestUserService(BaseTestCase):

    """Users Service tests"""
    
    def test_users(self):
        """
        Ensure ping route behaves correctly
        """
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code,200)    
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_user(self):
        """
        Ensure new user can be added into the db
        """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='mans',
                    email='mans@gmail.com'
                )),
                content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertIn('mans@gmail.com', data['message'])
        self.assertIn('success',data['status'])

    def test_add_user_invalid_json(self):
        """
        Ensure error is thrown if JSON object is
        invalid
        """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict()
            ), content_type='application/json')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        """
        Ensurean error is thrown if the JSON object doesn't
        have a username key
        """
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(email='mans@gmail.com')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('fail', data['status'])
            self.assertIn('Invalid payload', data['message'])

    
    def test_add_user_duplicate_user(self):
        """
        Ensure error is thrown if email or username
        exists
        """
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='mans',
                    email='mans@gmail.com')),
                content_type='application/json',
            )
        response = self.client.post(
            '/users',
            data=json.dumps(dict(
                username='mans',
                email='mans@gmail.com'
            )),
            content_type='application/json',
        )
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn(
            'Sorry. That email already exists.', data['message'])
        self.assertIn('fail', data['status'])

    def test_single_user(self):
        """
        Ensure a single user behaves correctly
        """
        user = add_user('mans', 'mans@gmail.com')
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue('created_at' in data['data'])
            self.assertIn('mans', data['data']['username'])
            self.assertIn('mans@gmail.com', data['data']['email'])
            self.assertIn('success', data['status'])

    def test_single_user_no_id(self):
        """
        Ensure error is thrown if and id is not provided
        """
        with self.client:
            response = self.client.get('/users/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_single_user_incorrect_id(self):
        """
        Ensure error is thrown if the id doesn't exist
        """
        with self.client:
            response = self.client.get('/users/999')
            data = json.loads(response.data.decode())
            self.assertIn('User does not exist', data['message'])
            self.assertIn('fail', data['status'])

    def test_all_users(self):
        """
        Ensure all users behaves correctly
        """
        add_user('mans', 'mans@gmail.com')
        add_user('wayua', 'wayua@gmail.com')
        with self.client:
            response = self.client.get('/users')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['users']), 2)
            self.assertTrue('created_at' in data['data']['users'][0])
            self.assertTrue('created_at' in data['data']['users'][1])
            self.assertIn('mans', data['data']['users'][0]['username'])
            self.assertIn(
            'mans@gmail.com', data['data']['users'][0]['email'])
            self.assertIn('wayua', data['data']['users'][1]['username'])
            self.assertIn(
            'wayua@gmail.com', data['data']['users'][1]['email'])
            self.assertIn('success', data['status'])