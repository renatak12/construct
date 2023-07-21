from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import Usuario , Fornecedor , Cliente , Endereco
from django.core.files.uploadedfile import SimpleUploadedFile
from accounts.views import Logado
from django.contrib.auth import login
import requests


class LoginTest(TestCase):
    def setUp(self):
        # Cria um usuário de teste para fazer o login
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')

    def test_login_with_valid_credentials(self):
        client = Client()

        response = client.post(reverse('accounts:login'), {'username': 'testuser', 'password': 'testpassword'})

        self.assertRedirects(response, reverse('accounts:logado'))

    def test_login_with_invalid_credentials(self):
        client = Client()

        response = client.post(reverse('accounts:login'), {'username': 'testuser', 'password': 'wrongpassword'})

        self.assertRedirects(response, reverse('accounts:login'))
        
class SignUpTest(TestCase):
    def test_signup_with_valid_credentials(self):
        client = Client()

        data = {
            'nome': 'Test User',
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'testpassword',
            'cpf': '12345678900',
            'telefone': '987654321',
        }

        response = client.post(reverse('accounts:signup'), data)

        self.assertRedirects(response, reverse('accounts:login'))

        self.assertTrue(Usuario.objects.filter(email=data['email']).exists())

    def test_signup_with_existing_email(self):
        Usuario.objects.create_user(username='existinguser', email='existing@example.com', password='existingpassword')

        client = Client()

        data = {
            'nome': 'Test User',
            'email': 'existing@example.com',
            'username': 'testuser',
            'password': 'testpassword',
            'cpf': '12345678900',
            'telefone': '987654321',
        }

        response = client.post(reverse('accounts:signup'), data)

        self.assertRedirects(response, reverse('accounts:signup'))

        

class LogadoTest(TestCase):
    def setUp(self):
        # Cria um usuário de teste para autenticação
        self.username = 'user1'
        self.password = 'password123'
        self.user = Usuario.objects.create_user(username=self.username, password=self.password)

        # Cria um cliente HTTP para simular as requisições
        self.client = Client()

        # URL reversa para a view 'logado'
        self.logado_url = reverse('accounts:logado')

    def test_logado_authenticated_user(self):
        # Teste quando o usuário está autenticado
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.logado_url)
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'accounts/logado.html')  
    def test_logado_unauthenticated_user(self):
        login_url = reverse('accounts:login')
        logado_url = reverse('accounts:logado')
        
        
        response = self.client.get(logado_url)
        
        self.assertEqual(response.status_code, 302)
        
        # Verifica se o redirecionamento é para a página de login
        self.assertRedirects(response, f"{login_url}?next={logado_url}")

class LogoutTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')

    def test_logout(self):
        
        self.client.login(username='testuser', password='testpassword')
        
       
        response = self.client.get(reverse('accounts:logout'))

       
        self.assertFalse(response.wsgi_request.user.is_authenticated)

       
        self.assertRedirects(response, reverse('pages:home'))

class ProfileTest(TestCase):
    def setUp(self):
        
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')

    def test_access_profile_authenticated_user(self):
        
        self.client.login(username='testuser', password='testpassword')

        
        response = self.client.get(reverse('accounts:profile'))

        
        self.assertTrue(response.wsgi_request.user.is_authenticated)

       
        self.assertEqual(response.status_code, 200)

    def test_update_profile_without_password_change(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('accounts:profile'), {'nome': 'Novo Nome', 'cpf': '111.222.333-44'})

        self.assertRedirects(response, reverse('accounts:profile'))

        self.user.refresh_from_db()

        self.assertEqual(self.user.username, 'testuser')  

    def test_update_profile_with_correct_password_change(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('accounts:profile'), {
            'nome': 'Novo Nome',
            'cpf': '111.222.333-44',
            'currentPassword': 'testpassword',  
            'newPassword': 'newtestpassword',   
            'renewPassword': 'newtestpassword'  
        })

        self.user.refresh_from_db()

        self.assertEqual(self.user.username, 'testuser') 

        self.assertTrue(self.user.check_password('newtestpassword'))

    def test_update_profile_with_incorrect_current_password(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('accounts:profile'), {
            'nome': 'Novo Nome',
            'cpf': '111.222.333-44',
            'currentPassword': 'wrongpassword',  
            'newPassword': 'newpassword',
            'renewPassword': 'newpassword',
        })

        self.assertRedirects(response, reverse('accounts:profile'))

        self.user.refresh_from_db()

        self.assertTrue(self.user.check_password('testpassword'))

    def test_update_profile_with_non_matching_new_passwords(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('accounts:profile'), {
            'nome': 'Novo Nome',
            'cpf': '111.222.333-44',
            'currentPassword': 'testpassword',
            'newPassword': 'newpassword',
            'renewPassword': 'nonmatchingpassword',  
        })

        self.assertRedirects(response, reverse('accounts:profile'))

        self.user.refresh_from_db()


        self.assertTrue(self.user.check_password('testpassword'))    

class UploadImageViewTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        
    def test_upload_image_with_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        # Cria uma imagem de teste
        image = SimpleUploadedFile("test_image.jpg", content=b"file_content", content_type="image/jpeg")

        response = self.client.post(reverse('accounts:upload_image'), {'nova_imagem': image})

        self.assertRedirects(response, reverse('accounts:profile'))

        self.user.refresh_from_db()

        self.assertIsNotNone(self.user.imagem)
        
class RemoveImageViewTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')

    def test_remove_image_with_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        image_file = SimpleUploadedFile("profile_image.jpg", b"file_content", content_type="image/jpeg")
        self.user.imagem = image_file
        self.user.save()

        self.assertTrue(self.user.imagem)

        response = self.client.get(reverse('accounts:remove_image'))

        self.assertRedirects(response, reverse('accounts:profile'))

        self.user.refresh_from_db()

        self.assertFalse(self.user.imagem)

#================================================================
# VIEWS FORNECEDORES

class CriarFornecedorTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_criar_fornecedor_with_valid_data(self):
        data = {
            'nome': 'Fornecedor Teste',
            'cnpj': '12345678901234',
            'telefone': '(99) 99999-9999',
            'email': 'fornecedor@teste.com',
        }

        response = self.client.post(reverse('accounts:criar_fornecedor'), data)

        self.assertRedirects(response, reverse('accounts:criar_fornecedor'))

        self.assertTrue(Fornecedor.objects.filter(nome=data['nome']).exists())

    def test_criar_fornecedor_with_invalid_data(self):
        data = {
            'nome': 'Fornecedor Teste',
            'cnpj': '',  # Cnpj em branco é inválido
            'telefone': '(99) 99999-9999',
            'email': 'fornecedor@teste.com',
        }

        response = self.client.post(reverse('accounts:criar_fornecedor'), data)

        self.assertEqual(response.status_code, 302)

        self.assertTrue(Fornecedor.objects.filter(nome=data['nome']).exists())

class ListarFornecedorTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_listar_fornecedor_page_loads(self):
        fornecedor1 = Fornecedor.objects.create(nome='Fornecedor 1', cnpj='12345678901234', telefone='(99) 99999-9999', email='fornecedor1@teste.com')
        fornecedor2 = Fornecedor.objects.create(nome='Fornecedor 2', cnpj='56789012345678', telefone='(99) 88888-8888', email='fornecedor2@teste.com')

        response = self.client.get(reverse('accounts:listar_fornecedor'))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, fornecedor1.nome)
        self.assertContains(response, fornecedor2.nome)

    def test_listar_fornecedor_empty_list(self):
        response = self.client.get(reverse('accounts:listar_fornecedor'))

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response, 'Nenhum fornecedor cadastrado.')

class EditarFornecedorTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_editar_fornecedor_page_loads(self):
        fornecedor = Fornecedor.objects.create(nome='Fornecedor 1', cnpj='12345678901234', telefone='(99) 99999-9999', email='fornecedor1@teste.com')

        response = self.client.get(reverse('accounts:editar_fornecedor', args=[fornecedor.id]))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, fornecedor.nome)
        self.assertContains(response, fornecedor.cnpj)
        self.assertContains(response, fornecedor.telefone)
        self.assertContains(response, fornecedor.email)

    def test_editar_fornecedor_post(self):
        fornecedor = Fornecedor.objects.create(nome='Fornecedor 1', cnpj='12345678901234', telefone='(99) 99999-9999', email='fornecedor1@teste.com')

        updated_nome = 'Novo Fornecedor'
        updated_cnpj = '98765432109876'
        updated_telefone = '(88) 88888-8888'
        updated_email = 'novo_fornecedor@teste.com'

        response = self.client.post(reverse('accounts:editar_fornecedor', args=[fornecedor.id]), {
            'nome': updated_nome,
            'cnpj': updated_cnpj,
            'telefone': updated_telefone,
            'email': updated_email,
        })

        self.assertRedirects(response, reverse('accounts:listar_fornecedor'))

        fornecedor.refresh_from_db()

        self.assertEqual(fornecedor.nome, updated_nome)
        self.assertEqual(fornecedor.cnpj, updated_cnpj)
        self.assertEqual(fornecedor.telefone, updated_telefone)
        self.assertEqual(fornecedor.email, updated_email)

class ExcluirFornecedorTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_excluir_fornecedor_page_loads(self):
        fornecedor = Fornecedor.objects.create(nome='Fornecedor 1', cnpj='12345678901234', telefone='(99) 99999-9999', email='fornecedor1@teste.com')

        response = self.client.get(reverse('accounts:excluir_fornecedor', args=[fornecedor.id]))

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response, fornecedor.nome)
        self.assertTrue(response, fornecedor.cnpj)
        self.assertTrue(response, fornecedor.telefone)
        self.assertTrue(response, fornecedor.email)

    def test_excluir_fornecedor_post(self):
        fornecedor = Fornecedor.objects.create(nome='Fornecedor 1', cnpj='12345678901234', telefone='(99) 99999-9999', email='fornecedor1@teste.com')

        response = self.client.post(reverse('accounts:excluir_fornecedor', args=[fornecedor.id]))

        self.assertRedirects(response, reverse('accounts:listar_fornecedor'))

        self.assertFalse(Fornecedor.objects.filter(id=fornecedor.id).exists())

#================================================================
# VIEWS CLIENTES

class CriarClienteTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_criar_cliente_page_loads(self):
        response = self.client.get(reverse('accounts:criar_cliente'))

        self.assertEqual(response.status_code, 200)

    def test_criar_cliente_post(self):
        data = {
            'nome': 'Cliente Teste',
            'telefone': '(99) 99999-9999',
            'cpf': '12345678901',
            'email': 'cliente@teste.com',
            'logradouro': 'Rua Teste',
            'numero': '123',
            'cep': '12345-678',
        }

        class MockResponse:
            status_code = 200

            def json(self):
                return {'localidade': 'Teste', 'uf': 'TT'}

        def mock_get(url):
            return MockResponse()

        original_requests_get = requests.get
        requests.get = mock_get

        response = self.client.post(reverse('accounts:criar_cliente'), data=data)

        requests.get = original_requests_get

        self.assertRedirects(response, reverse('accounts:criar_cliente'))

        self.assertTrue(Cliente.objects.filter(nome=data['nome']).exists())
        self.assertTrue(Cliente.objects.filter(telefone=data['telefone']).exists())
        self.assertTrue(Cliente.objects.filter(cpf=data['cpf']).exists())
        self.assertTrue(Cliente.objects.filter(email=data['email']).exists())

        cliente = Cliente.objects.get(nome=data['nome'])
        self.assertTrue(Endereco.objects.filter(id=cliente.endereco.id).exists())
        endereco = Endereco.objects.get(id=cliente.endereco.id)
        self.assertEqual(endereco.logradouro, data['logradouro'])
        self.assertEqual(endereco.numero, data['numero'])
        self.assertEqual(endereco.cep, data['cep'])
        self.assertEqual(endereco.cidade, 'Teste')
        self.assertEqual(endereco.estado, 'TT')

class ListarClientesTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_listar_clientes_page_loads(self):
        response = self.client.get(reverse('accounts:listar_clientes'))

        self.assertEqual(response.status_code, 200)

    def test_listar_clientes_displayed(self):
        Cliente.objects.create(nome='Cliente 1', telefone='(99) 99999-9999', cpf='12345678901', email='cliente1@teste.com')
        Cliente.objects.create(nome='Cliente 2', telefone='(88) 88888-8888', cpf='98765432109', email='cliente2@teste.com')

        response = self.client.get(reverse('accounts:listar_clientes'))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Cliente 1')
        self.assertContains(response, 'Cliente 2')
        self.assertTrue(response, '(99) 99999-9999')
        self.assertTrue(response, '(88) 88888-8888')
        self.assertTrue(response, '12345678901')
        self.assertTrue(response, '98765432109')
        self.assertTrue(response, 'cliente1@teste.com')
        self.assertTrue(response, 'cliente2@teste.com')

class EditarClienteTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_editar_cliente_page_loads(self):
        cliente = Cliente.objects.create(nome='Cliente Teste', telefone='(99) 99999-9999', cpf='12345678901', email='cliente@teste.com')
        endereco = Endereco.objects.create(logradouro='Rua A', numero='123', cep='12345-678', cidade='Cidade Teste', estado='UF')
        cliente.endereco = endereco
        cliente.save()

        response = self.client.get(reverse('accounts:editar_cliente', kwargs={'cliente_id': cliente.id}))

        self.assertEqual(response.status_code, 200)

    def test_editar_cliente_save_changes(self):
        cliente = Cliente.objects.create(nome='Cliente Teste', telefone='(99) 99999-9999', cpf='12345678901', email='cliente@teste.com')
        endereco = Endereco.objects.create(logradouro='Rua A', numero='123', cep='12345-678', cidade='Cidade Teste', estado='UF')
        cliente.endereco = endereco
        cliente.save()

        data = {
            'nome': 'Novo Nome',
            'telefone': '(88) 88888-8888',
            'cpf': '98765432109',
            'email': 'novo_email@teste.com',
            'logradouro': 'Rua B',
            'numero': '456',
            'cep': '98765-432',
            'cidade': 'Outra Cidade',
            'estado': 'NY',
        }
        response = self.client.post(reverse('accounts:editar_cliente', kwargs={'cliente_id': cliente.id}), data)

        updated_cliente = Cliente.objects.get(id=cliente.id)
        self.assertEqual(updated_cliente.nome, 'Novo Nome')
        self.assertEqual(updated_cliente.telefone, '(88) 88888-8888')
        self.assertEqual(updated_cliente.cpf, '98765432109')
        self.assertEqual(updated_cliente.email, 'novo_email@teste.com')
        self.assertEqual(updated_cliente.endereco.logradouro, 'Rua B')
        self.assertEqual(updated_cliente.endereco.numero, '456')
        self.assertEqual(updated_cliente.endereco.cep, '98765-432')
        self.assertEqual(updated_cliente.endereco.cidade, 'Outra Cidade')
        self.assertEqual(updated_cliente.endereco.estado, 'NY')

        self.assertRedirects(response, reverse('accounts:listar_clientes'))

class ExcluirClienteTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_excluir_cliente_page_loads(self):
        cliente = Cliente.objects.create(nome='Cliente Teste', telefone='(99) 99999-9999', cpf='12345678901', email='cliente@teste.com')

        response = self.client.get(reverse('accounts:excluir_cliente', kwargs={'cliente_id': cliente.id}))

        self.assertEqual(response.status_code, 200)

    def test_excluir_cliente(self):
        cliente = Cliente.objects.create(nome='Cliente Teste', telefone='(99) 99999-9999', cpf='12345678901', email='cliente@teste.com')

        response = self.client.post(reverse('accounts:excluir_cliente', kwargs={'cliente_id': cliente.id}))

        self.assertFalse(Cliente.objects.filter(id=cliente.id).exists())

        self.assertRedirects(response, reverse('accounts:listar_clientes'))
