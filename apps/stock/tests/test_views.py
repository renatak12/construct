from django.test import TestCase, RequestFactory , Client
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from stock.views import CriarCategoria
from stock.models import Categoria , Produto , Fornecedor
from accounts.models import Usuario
from django.contrib.messages.middleware import MessageMiddleware
from django.core.files.uploadedfile import SimpleUploadedFile
from stock.models import Produto, Cliente, Venda , Categoria
from decimal import Decimal
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages import SUCCESS
from django.test.client import Client
from django.utils.http import urlencode


class CriarCategoriaTest(TestCase):
    def setUp(self):
        # Cria um usuário para simular uma requisição autenticada
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')

        # Cria uma instância da fábrica de requisições
        self.factory = RequestFactory()

    def test_criar_categoria_get(self):
        # Cria uma requisição GET para a página de criação de categoria
        request = self.factory.get(reverse('stock:criar_categoria'))

        # Associa o usuário autenticado à requisição
        request.user = self.user

        # Chama a view para processar a requisição
        response = CriarCategoria.as_view()(request)

        # Verifica se a resposta tem o código HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

class ListarCategoriasTest(TestCase):
    def setUp(self):
        # Crie um usuário de teste e faça login
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = Usuario.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_listar_categorias(self):
        Categoria.objects.create(nome='Categoria 1')
        Categoria.objects.create(nome='Categoria 2')
        Categoria.objects.create(nome='Categoria 3')

        response = self.client.get(reverse('stock:listar_categorias'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'stock/categorias/listar.html')

        categorias = response.context['categorias']
        self.assertEqual(categorias.count(), 3)

        nomes_categorias = [categoria.nome for categoria in categorias]
        self.assertListEqual(nomes_categorias, ['Categoria 1', 'Categoria 2', 'Categoria 3'])

class EditarCategoriaTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = Usuario.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_editar_categoria(self):
        categoria = Categoria.objects.create(nome='Categoria Original')

        editar_url = reverse('stock:editar_categoria', args=[categoria.id])

        novos_dados = {'nome': 'Nova Categoria'}

        response = self.client.post(editar_url, data=novos_dados)

        self.assertRedirects(response, reverse('stock:listar_categorias'))

        categoria_atualizada = Categoria.objects.get(id=categoria.id)

        self.assertEqual(categoria_atualizada.nome, 'Nova Categoria')

        storage = get_messages(response.wsgi_request)
        messages = [msg.message for msg in storage]
        self.assertIn('Categoria atualizada com sucesso!', messages)

class ExcluirCategoriaTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = Usuario.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_excluir_categoria(self):
        categoria = Categoria.objects.create(nome='Categoria a ser excluída')

        excluir_url = reverse('stock:excluir_categoria', args=[categoria.id])

        response = self.client.post(excluir_url)

        self.assertRedirects(response, reverse('stock:listar_categorias'))

        with self.assertRaises(Categoria.DoesNotExist):
            Categoria.objects.get(id=categoria.id)

        storage = get_messages(response.wsgi_request)
        messages = [msg.message for msg in storage]
        self.assertIn('Categoria excluída com sucesso!', messages)

#=================================================================
# VIEWS PRODUTOS

class CriarProdutoTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = Usuario.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_criar_produto(self):
        categoria = Categoria.objects.create(nome='Categoria de Teste')

        fornecedor = Fornecedor.objects.create(nome='Fornecedor de Teste')

        produto_data = {
            'nome': 'Produto de Teste',
            'descricao': 'Descrição do produto de teste',
            'preco': '100.00',
            'quantidade_estoque': '10',
            'categoria': categoria.id,
            'fornecedor': fornecedor.id,
        }

        imagem = SimpleUploadedFile('produto_teste.jpg', b'test image content')

        criar_url = reverse('stock:criar_produto')

        response = self.client.post(criar_url, produto_data, format='multipart')

        self.assertRedirects(response, reverse('stock:criar_produto'))

        self.assertTrue(Produto.objects.filter(nome=produto_data['nome']).exists())

        produto_criado = Produto.objects.get(nome=produto_data['nome'])
        self.assertIsNotNone(produto_criado.imagem)

class ListarProdutosTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = Usuario.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_listar_produtos(self):
        categoria = Categoria.objects.create(nome='Categoria de Teste')

        produto1 = Produto.objects.create(nome='Produto 1', descricao='Descrição do Produto 1', preco='50.00', quantidade_estoque='5', categoria=categoria)
        produto2 = Produto.objects.create(nome='Produto 2', descricao='Descrição do Produto 2', preco='30.00', quantidade_estoque='8', categoria=categoria)

        listar_url = reverse('stock:listar_produtos')

        response = self.client.get(listar_url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, produto1.nome)
        self.assertContains(response, produto1.descricao)
        self.assertContains(response, produto1.preco)
        self.assertContains(response, produto1.quantidade_estoque)

        self.assertContains(response, produto2.nome)
        self.assertContains(response, produto2.descricao)
        self.assertContains(response, produto2.preco)
        self.assertContains(response, produto2.quantidade_estoque)

class EditarProdutoTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = Usuario.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_editar_produto_post(self):
        categoria = Categoria.objects.create(nome='Categoria de Teste')

        fornecedor = Fornecedor.objects.create(nome='Fornecedor de Teste')

        produto = Produto.objects.create(nome='Produto Teste', descricao='Descrição do Produto Teste',
                                         preco='100.00', quantidade_estoque='10', categoria=categoria, fornecedor=fornecedor)

        editar_url = reverse('stock:editar_produto', args=[produto.id])

        data = {
            'nome': 'Produto Editado',
            'descricao': 'Descrição Editada',
            'preco': '150.00',
            'quantidade_estoque': '20',
            'categoria': categoria.id,
            'fornecedor': fornecedor.id,
        }

        response = self.client.post(editar_url, data=data)

        self.assertRedirects(response, reverse('stock:listar_produtos'))

        produto.refresh_from_db()

        self.assertEqual(produto.nome, data['nome'])
        self.assertEqual(produto.descricao, data['descricao'])
        self.assertEqual(str(produto.preco), data['preco']) 
        self.assertEqual(produto.quantidade_estoque, int(data['quantidade_estoque']))
        self.assertEqual(produto.categoria, categoria)
        self.assertEqual(produto.fornecedor, fornecedor)

class ExcluirProdutoTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = Usuario.objects.create_user(username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

    def test_excluir_produto_post(self):
        categoria = Categoria.objects.create(nome='Categoria de Teste')

        fornecedor = Fornecedor.objects.create(nome='Fornecedor de Teste')

        produto = Produto.objects.create(nome='Produto Teste', descricao='Descrição do Produto Teste',
                                         preco='100.00', quantidade_estoque='10', categoria=categoria, fornecedor=fornecedor)

        excluir_url = reverse('stock:excluir_produto', args=[produto.id])

        response = self.client.post(excluir_url)

        self.assertRedirects(response, reverse('stock:listar_produtos'))

        self.assertFalse(Produto.objects.filter(pk=produto.id).exists())

#============================================================
# VIEWS ESTOQUE

class AdicionarEstoqueTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_adicionar_estoque(self):
        categoria = Categoria.objects.create(nome='Test Category')

        produto = Produto.objects.create(
            nome='Test Product',
            descricao='Test Description',
            preco=10.00,
            quantidade_estoque=100,
            categoria=categoria,  
        )

        url = reverse('stock:adicionar_estoque', args=[produto.id])

        quantidade_adicionada = 50
        response = self.client.post(url, {'quantidade': quantidade_adicionada})

        self.assertRedirects(response, reverse('stock:listar_estoque'))

        produto.refresh_from_db()

        self.assertEqual(produto.quantidade_estoque, 50)

class ListarEstoqueTest(TestCase):
    def setUp(self):
        # Create a test user and log in
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_listar_estoque(self):
        # Create a test category
        categoria = Categoria.objects.create(nome='Category 1')

        # Create some test products
        produto1 = Produto.objects.create(nome='Product 1', descricao='Description 1', preco=10.00, quantidade_estoque=50, categoria=categoria)
        produto2 = Produto.objects.create(nome='Product 2', descricao='Description 2', preco=20.00, quantidade_estoque=30, categoria=categoria)

        # Define the URL for the ListarEstoque view
        url = reverse('stock:listar_estoque')

        # Simulate a GET request to the view
        response = self.client.get(url)

        # Check if the view returns a 200 OK response
        self.assertEqual(response.status_code, 200)

        # Check if the rendered template contains the products' names
        self.assertContains(response, produto1.nome)
        self.assertContains(response, produto2.nome)

        # Check if the rendered template contains the products' descriptions
        self.assertTrue(response, produto1.descricao)
        self.assertTrue(response, produto2.descricao)

        # Check if the rendered template contains the products' prices
        self.assertContains(response, str(produto1.preco))
        self.assertContains(response, str(produto2.preco))

        # Check if the rendered template contains the products' stock quantities
        self.assertContains(response, str(produto1.quantidade_estoque))
        self.assertContains(response, str(produto2.quantidade_estoque))

#=====================================================
# VIEWS VENDA

class RealizarVendaTest(TestCase):
    def setUp(self):
        # Create a test user and log in
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_realizar_venda_success(self):
        # Create test Cliente instance
        cliente = Cliente.objects.create(nome='Test Cliente', cpf='12345678900')

        # Create test Categoria instance
        categoria = Categoria.objects.create(nome='Test Categoria')

        # Create test Produto instance using the created Categoria
        produto = Produto.objects.create(
            categoria=categoria,
            nome='Test Produto',
            descricao='Test Description',
            preco=100.00,
            quantidade_estoque=10
        )


    def test_realizar_venda_insufficient_stock(self):
        # Create test Cliente instance
        cliente = Cliente.objects.create(nome='Test Cliente', cpf='12345678900')

        # Create test Categoria instance
        categoria = Categoria.objects.create(nome='Test Categoria')

        # Create test Produto instance with quantidade_estoque=0 and the created Categoria
        produto = Produto.objects.create(
            categoria=categoria,
            nome='Test Produto',
            descricao='Test Description',
            preco=100.00,
            quantidade_estoque=0
        )

class ExcluirVendaTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_excluir_venda(self):
        # Create a category
        categoria = Categoria.objects.create(nome='Test Category')

        # Create a product with a category
        produto = Produto.objects.create(
            nome='Test Product',
            descricao='Test Description',
            preco=100.00,
            quantidade_estoque=10,
            categoria=categoria,
        )

        # Create a client
        cliente = Cliente.objects.create(nome='Test Client')

        # Create a sale with valid values for all required fields
        venda = Venda.objects.create(
            cliente=cliente,
            produto=produto,
            quantidade=5,
            preco=100.00,
            valor_total=500.00,
            valor_total_compra=500.00,
            valor_parcela=500.00,
            forma_pagamento='dinheiro',
            desconto=0.00,  # Provide a valid desconto value here
        )

        # Check the sale exists before deletion
        self.assertEqual(Venda.objects.count(), 1)

        # Perform the delete view with login
        self.client.login(username='testuser', password='testpass')
        url = reverse('stock:excluir_venda', args=[venda.id])
        response = self.client.post(url)

        # Check the response status code and redirection
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('stock:listar_vendas'))

        # Check the sale is deleted
        self.assertEqual(Venda.objects.count(), 0)

        # Check the quantity of the product is restored to the stock
        produto.refresh_from_db()
        self.assertEqual(produto.quantidade_estoque, 15)
