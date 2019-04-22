import json

from tests.base import BaseTestCase


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
