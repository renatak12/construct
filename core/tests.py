from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class CoreViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_home_view(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login_view(self):
        response = self.client.get(reverse('core:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_signup_view(self):
        response = self.client.get(reverse('core:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_logado_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('core:logado'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/logado.html')

