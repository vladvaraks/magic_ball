from django.test import TestCase
from django.contrib.auth.models import User

class TestMagicApp(TestCase):

    def setUp(self):
        self.credentials = {
            'username': '!qweq!!~~2132'}

    def test_login_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        response = self.client.post('/', self.credentials, format='text/html', follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_question(self):
        response = self.client.get('/question/')
        self.assertEqual(response.status_code, 302)
