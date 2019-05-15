import json
import time

from flask_users import db
from flask_users.api.models import User
from tests.base import BaseTestCase
from tests.utils import add_user


class TestAuthBlueprint(BaseTestCase):
    
    def test_user_registration(self):
        with self.client:
            reg_response = self.client.post(
                '/auth/register',
                data=json.dumps(dict(
                    username='mans',
                    email='mans@gmail.com',
                    password='4321drowssap'
                )),
                content_type='application/json'
            )
            reg_data = json.loads(reg_response.data.decode())
            self.assertTrue(data['status']== 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(data['auth_token'])
            self.assertEqual(reg_response.status_code, 201)
            self.assertTrue(reg_response.content_type == 'application/json')

    def test_user_registration_duplicate_email(self):
        add_user('mans', 'mans@gmail.com', '4321drowssap')
        with self.client:
            response = self.client.post(
                '/auth/register',
                data=json.dumps(dict(
                    username='womans',
                    email='mans@gmail.com',
                    password='4321drowssap'
                )),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertTrue(response.content_type == 'application/json')
            self.assertIn('Sorry. That user already exists.', data['message'])
            self.assertIn('fail', data['status'])

    def test_user_registration_duplicate_name(self):
        add_user('mans', 'mans@gmail.com','4321drowssap')
        with self.client:
            response = self.client.post(
                '/auth/register',
                data=json.dumps(dict(
                    username='mans',
                    email='womans@gmail.com',
                    password='4321drowssap'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertTrue(response.content_type == 'application/json')
            self.assertIn('Sorry. That user already exists.', data['message'])
            self.assertIn('fail', data['status'])
    
    def test_user_registration_invalid_json(self):
        with self.client:
            response = self.client.post(
                '/auth/register',
                data=json.loads(dict()),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid payload.', data['message'])
        self.assertIn('fail', data['status'])

    def test_user_registration_invalid_json_keys_no_username(self):
        with self.client:
            response = self.client.post(
                '/auth/register',
                data=json.dumps(dict(email='test@test.com', password='test')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_user_registration_invalid_json_keys_no_email(self):
        with self.client:
            response = self.client.post(
                '/auth/register',
                data=json.dumps(dict(
                    username='justatest', password='test')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_user_registration_invalid_json_keys_no_password(self):
        with self.client:
            response = self.client.post(
                '/auth/register',
                data=json.dumps(dict(
                    username='justatest', email='test@test.com')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_registered_user_login(self):
        with self.client:
            user = add_user('mans', 'mans@gmail.com', 'password1234')
            response = self.client.post(
                '/auth/login',
                data=json.loads(dict(
                    email='mans@gmail.com',
                    password='password1234'
                )),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully logged in.')
            self.assertTrue(data['auth_token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200) 

    def test_not_registered_user_login(self):
        with self.client:
            response = self.client.post(
                '/auth/login',
                data=json.dumps(dict(
                    email='curtis@gmail.com',
                    password='4321drowssap'
                )),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'User does not exist.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 404)

    def test_valid_logout(self):
        add_user('mans', 'mans@gmail.com', '4321drowssap')
        with self.client:
            # user login
            login_resp = self.client.post(
                'auth/login',
                data=json.dumps(dict(
                    email='mans@gmail.com',
                    password='4321drowssap'
                )),
                content_type='application/json',
            )

            # valid logout
            logout_response = self.client.post(
                '/auth/logout',
                headers=dict(
                    Authorization='Bearer ' + json.loads(login_resp.data.decode())['auth_token']
                )
            )
            logout_data = json.loads(logout_response.data.decode())
            self.assertTrue(data['message'] == 'Successfully logged out.')
            self.assertTrue(data['status'] == 'success')
            self.assertEqual(logout_response.status_code, 200)
    
    def test_invalid_logout_expired_token(self):
        add_user('mans', 'mans@gmail.com', '4321drowssap')
        with self.client:
            # user login
            login_resp = self.client.post(
                'auth/login',
                data=json.dumps(dict(
                    email='mans@gmail.com',
                    password='4321drowssap'
                )),
                content_type='application/json',
            )

            # valid logout
            logout_response = self.client.post(
                '/auth/logout',
                headers=dict(
                    Authorization='Bearer ' + json.loads(login_resp.data.decode())['auth_token']
                )
            )
            time.sleep(45)
            logout_data = json.loads(logout_response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Signature expired. Please login again.')
            self.assertEqual(logout_response.status_code, 401)
    
    def test_invalid_logout(self):
        with self.client:
            response = self.client.get(
                '/auth/logout',
                headers=dict(Authorization='Bearer invalid'))
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'error')
            self.assertTrue(
                data['message'] == 'Invalid token. Please log in again.')
            self.assertEqual(response.status_code, 401)

    def test_user_status(self):
        add_user('mans', 'mans@gmail.com', '4321drowssap')
        with self.client:
            resp_login = self.client.post(
                '/auth/login',
                data=json.dumps(dict(
                    email='mans@gmail.com',
                    password='4321drowssap'
                )),
                content_type='application/json',
            )
            status_response = self.client.get(
                '/auth/status',
                headers=dict(
                    Authorization='Bearer ' + json.loads(resp_login.data.decode)['auth_token']
                )
            )

            data =  json.loads(status_response.data.decode())
            self.assertEqual(status_response.status_code, 200)
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['data'] is not None)
            self.assertTrue(data['data']['username'] == 'mans')
            self.assertTrue(data['data']['email'] == 'mans@gmail.com')
            self.assertTrue(data['data']['active'] is True)
            self.assertTrue(data['data']['created_at'])

    def test_user_status_invalid(self):
        with self.client:
            response = self.client.get(
                '/auth/status',
                headers=dict(
                    Authorization='Bearer invalid'))
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Invalid token. Please login again.')
            self.assertEqual(response.status_code, 401)