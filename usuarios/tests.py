from django.test import TestCase
from unittest.case import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from .models import Users
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


class LoginTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = Users.objects.create_user(
            username='vitoria@gmail.com',
            password='senha321'
        )
    
    def test_login_GET(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_login_POST_valid(self):
        data = {
            'email': 'vitoria@gmail.com',
            'senha': 'senha321'
        }
        response = self.client.post(self.url, data=data)
        self.assertRedirects(response, reverse('index'))
    
    def test_login_POST_invalid(self):
        data = {
            'email': 'vitoria@gmail.com',
            'senha': 'senha123'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'Usuário inválido')


class TestUsuarioModel(TestCase):
    def setUp(self):
        Users.objects.create_user(username='vitoria@gmail.com', password='senha321')

    def test_nome_usuario(self):
        usuario = Users.objects.get(id=1)
        self.assertEqual(usuario.username, 'vitoria@gmail.com')

    def test_senha_usuario(self):
        usuario = Users.objects.get(id=1)
        self.assertTrue(usuario.check_password('senha321'))

    def test_administrador_usuario(self):
        usuario = Users.objects.get(id=1)
        self.assertFalse(usuario.is_superuser)