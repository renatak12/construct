from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from core.models import Usuario, Endereco, Material, Fornecedor, Compra, Produto

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

class EnderecoTest(TestCase):
    def setUp(self):
        self.endereco = Endereco.objects.create(
            logradouro='Rua Teste',
            numero='123',
            cidade='Cidade Teste',
            estado='SP'
        )

    def test_str(self):
        endereco_str = str(self.endereco)
        self.assertEqual(endereco_str, 'SP')

class UsuarioTest(TestCase):
    def setUp(self):
        # Cria um endereço para associar ao usuário
        self.endereco = Endereco.objects.create(
            logradouro='Rua Teste',
            numero='123',
            cidade='Cidade Teste',
            estado='SP'
        )

        # Cria um arquivo temporário para simular o upload de uma imagem
        imagem_temp = SimpleUploadedFile("usuario_imagem.jpg", b"file_content", content_type="image/jpeg")

        # Cria um usuário de exemplo
        self.usuario = Usuario.objects.create(
            username='testuser',
            nome='Nome do Teste',
            cpf='123456789',
            telefone='987654321',
            imagem=imagem_temp,
            endereco=self.endereco,
            email='test@example.com'
        )

    def test_primeiro_nome(self):
        primeiro_nome = self.usuario.primeiro_nome()
        self.assertEqual(primeiro_nome, 'Nome')

class MaterialTest(TestCase):
    def setUp(self):
        # Cria um material de exemplo
        self.material = Material.objects.create(
            nome='Material Teste',
            descricao='Descrição do Material Teste'
        )

    def test_str(self):
        nome_material = str(self.material)
        self.assertEqual(nome_material, 'Material Teste')

class FornecedorTest(TestCase):
    def setUp(self):
        # Cria um fornecedor de exemplo
        self.fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            cnpj='12345678901234',
            telefone='1234567890',
            email='fornecedor@teste.com'
        )

    def test_primeiro_nome(self):
        primeiro_nome = self.fornecedor.primeiro_nome()
        self.assertEqual(primeiro_nome, 'Fornecedor')

class CompraTest(TestCase):
    def setUp(self):
        # Cria um fornecedor de exemplo
        self.fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            cnpj='12345678901234',
            telefone='1234567890',
            email='fornecedor@teste.com'
        )

        # Cria um material de exemplo
        self.material = Material.objects.create(
            nome='Material Teste',
            descricao='Descrição do Material Teste'
        )

        # Cria uma compra de exemplo
        self.compra = Compra.objects.create(
            fornecedor=self.fornecedor,
            material=self.material,
            quantidade=10,
            preco_custo=100.0
        )

    def test_str(self):
        compra_str = str(self.compra)
        self.assertEqual(compra_str, 'Material Teste')

class ProdutoTest(TestCase):
    def setUp(self):
        # Cria um fornecedor de exemplo
        self.fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            cnpj='12345678901234',
            telefone='1234567890',
            email='fornecedor@teste.com'
        )

        # Cria um material de exemplo
        self.material = Material.objects.create(
            nome='Material Teste',
            descricao='Descrição do Material Teste'
        )

        # Cria um produto de exemplo
        self.produto = Produto.objects.create(
            nome='Produto Teste',
            preco_unitario=10.0,
            fornecedor=self.fornecedor,
            material=self.material
        )

    def test_str(self):
        produto_str = str(self.produto)
        self.assertEqual(produto_str, 'Produto Teste')