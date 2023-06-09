from django.test import TestCase, Client
from django.urls import reverse
from .models import Users
from django.contrib.messages import get_messages, get_level



class LoginTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = Users.objects.create_user(
            username='vitoria@gmail.com',
            password='senha321'
        )
    
    def test_login_POST_valid(self):
        data = {
            'email': 'vitoria@gmail.com',
            'senha': 'senha321'
        }
        response = self.client.post(self.url, data=data, follow=True)
        self.assertRedirects(response, reverse('index'))
        
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].level_tag, 'alert-success')
        self.assertEqual(messages[0].message, 'Usuário logado com sucesso')

class CadastrarVendedorTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('cadastrar_vendedor')
        self.user = Users.objects.create_user(
            username='renatak12',
            password='0212',
            is_staff=True
        )

    def test_cadastrar_vendedor_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastrar_vendedor.html')

    def test_cadastrar_vendedor_POST_valid(self):
        self.client.force_login(self.user)
        data = {
            'nome': 'Vitoria',
            'sobrenome': 'Santos',
            'email': 'vitorias@gmail.com',
            'senha': 'senha321'
        }
        response = self.client.post(self.url, data=data)
        self.assertRedirects(response, reverse('cadastrar_vendedor'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].level_tag, 'alert-success')
        self.assertEqual(messages[0].message, 'Conta criada')

    def test_cadastrar_vendedor_POST_invalid(self):
        self.client.force_login(self.user)
        user = Users.objects.create_user(
            username='vitoria@gmail.com',
            email='vitoria@gmail.com',
            password='senha321',
            first_name='Vitoria',
            last_name='Souza',
            cargo='V'
        )
        data = {
            'nome': 'Vitoria',
            'sobrenome': 'Souza',
            'email': 'vitoria@gmail.com',
            'senha': 'senha321'
        }
        response = self.client.post(self.url, data=data)
        self.assertRedirects(response, reverse('cadastrar_vendedor'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].level_tag, 'alert-danger')
        self.assertEqual(messages[0].message, 'Email já existe')
    

    def test_excluir_usuario(self):
        vendedor = Users.objects.create(username='ana@gmail.com', email='ana@gmail.com', cargo='V')
        url = reverse('excluir_usuario', args=[vendedor.id])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('cadastrar_vendedor'))
        vendedor_exists = Users.objects.filter(id=vendedor.id).exists()
        self.assertFalse(vendedor_exists)
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].level_tag, 'alert-success')
        self.assertEqual(messages[0].message, 'Vendedor excluido com sucesso')

class TestUsuarioModel(TestCase):

    def setUp(self):
        Users.objects.create_user(username='marcos', password='senha321')

    def test_nome_usuario(self):
        usuario = Users.objects.get(id=1)
        self.assertEqual(usuario.username, 'marcos')

    def test_senha_usuario(self):
        usuario = Users.objects.get(id=1)
        self.assertTrue(usuario.check_password('senha321'))

    def test_administrador_usuario(self):
        usuario = Users.objects.get(id=1)
        self.assertFalse(usuario.is_superuser)