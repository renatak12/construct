from django.test import TestCase, Client
from vendas.models import Produto, Categoria, Fornecedor, Compra, ItemCompra
from usuarios.models import Usuario
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from decimal import Decimal
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect, get_object_or_404
from vendas.views import cadastrar_categoria
from django.core.files.uploadedfile import SimpleUploadedFile

class CategoriaViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cadastrar_categoria(self):
        # Define os dados do formulário
        form_data = {
            'nome': 'Nova Categoria',
        }

        # Envia uma solicitação POST para cadastrar a categoria
        response = self.client.post(reverse('cadastrar_categoria'), form_data)

        # Verifica se a resposta redireciona para a página de listagem de categorias
        self.assertRedirects(response, reverse('listar_categorias'))

        # Verifica se a categoria foi criada no banco de dados
        categoria_criada = Categoria.objects.get(nome='Nova Categoria')
        self.assertEqual(categoria_criada.nome, 'Nova Categoria')

        # Verifica se a página de listagem de categorias é exibida corretamente
        response = self.client.get(reverse('listar_categorias'))
        self.assertContains(response, 'Nova Categoria')


    def test_listar_categorias(self):
        # Cria algumas categorias para testar
        Categoria.objects.create(nome='Categoria 1')
        Categoria.objects.create(nome='Categoria 2')
        Categoria.objects.create(nome='Categoria 3')

        # Envia uma solicitação GET para listar as categorias
        response = self.client.get(reverse('listar_categorias'))

        # Verifica se a resposta tem o status code 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifica se a página contém as categorias corretas
        self.assertContains(response, 'Categoria 1')
        self.assertContains(response, 'Categoria 2')
        self.assertContains(response, 'Categoria 3')

        # Verifica se o número de categorias exibidas é o esperado
        self.assertEqual(len(response.context['categorias']), 3)


    def test_editar_categoria(self):
        # Cria uma categoria para testar
        categoria = Categoria.objects.create(nome='Categoria 1')

        # Dados a serem enviados no formulário de edição
        dados = {'nome': 'Categoria Editada'}

        # Envia uma solicitação POST para editar a categoria
        response = self.client.post(reverse('editar_categoria', args=[categoria.id]), data=dados)

        # Verifica se a resposta redireciona para a página de listagem de categorias
        self.assertRedirects(response, reverse('listar_categorias'))

        # Atualiza o objeto categoria com os dados do banco de dados
        categoria.refresh_from_db()

        # Verifica se a categoria foi atualizada corretamente
        self.assertEqual(categoria.nome, 'Categoria Editada')


    def test_excluir_categoria(self):
        # Cria uma categoria para testar
        categoria = Categoria.objects.create(nome='Categoria 1')

        # Envia uma solicitação POST para excluir a categoria
        response = self.client.post(reverse('excluir_categoria', args=[categoria.id]))

        # Verifica se a resposta redireciona para a página de listagem de categorias
        self.assertRedirects(response, reverse('listar_categorias'))

        # Verifica se a categoria foi excluída corretamente
        self.assertFalse(Categoria.objects.filter(id=categoria.id).exists())

class CadastrarProdutoTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cadastrar_produto(self):
        # Cria categorias e fornecedores para testar
        categoria = Categoria.objects.create(nome='Categoria 1')
        fornecedor = Fornecedor.objects.create(nome='Fornecedor 1')

        # Dados do produto a ser cadastrado
        produto_data = {
            'nome': 'Produto 1',
            'descricao': 'Descrição do Produto 1',
            'categoria': categoria.id,
            'fornecedor': fornecedor.id,
            'preco_compra': '10.00',
            'preco_venda': '20.00'
        }

        # Envia uma solicitação POST para cadastrar o produto
        response = self.client.post(reverse('cadastrar_produto'), data=produto_data)

        # Verifica se a resposta redireciona para a página de listagem de produtos
        self.assertRedirects(response, reverse('listar_produtos'))

        # Verifica se o produto foi cadastrado corretamente
        self.assertTrue(Produto.objects.filter(nome='Produto 1').exists())

class DetalharProdutoTest(TestCase):
    def test_detalhar_produto(self):
        # Cria uma categoria para associar ao produto
        categoria = Categoria.objects.create(nome='Categoria 1')
        # Cria um fornecedor para associar ao produto
        fornecedor = Fornecedor.objects.create(nome='Fornecedor 1')
        # Cria um arquivo temporário para simular o upload de uma imagem
        imagem_temp = SimpleUploadedFile("produto_imagem.jpg", b"file_content", content_type="image/jpeg")

        # Cria um produto para testar, associado à categoria criada
        produto = Produto.objects.create(
        nome='Produto 1',
        descricao='Descrição do Produto 1',
        categoria_id=categoria.id,
        fornecedor_id=fornecedor.id,  # Fornecer o ID da categoria
        preco_compra=100.0,
        preco_venda=200.0,
        imagem=imagem_temp 
    )

        # Envia uma solicitação GET para detalhar o produto
        response = self.client.get(reverse('detalhar_produto', args=[produto.id]))

        # Verifica se a resposta possui o código de status 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifica se o produto correto está sendo exibido no contexto do template
        self.assertEqual(response.context['produto'], produto)

        # Verifica se o template correto está sendo usado para renderizar a página
        self.assertTemplateUsed(response, 'produtos/detalhar_produto.html')

class ListarProdutoTest(TestCase):    
    def setUp(self):
        self.client = Client()
        
        # Cria um usuário de teste
        self.user = Usuario.objects.create_user(username='testuser', password='testpass')
        
        # Cria uma categoria para associar ao produto
        categoria = Categoria.objects.create(nome='Categoria 1')
        categoria2 = Categoria.objects.create(nome='Categoria 2')
        
        # Cria um fornecedor para associar ao produto
        fornecedor = Fornecedor.objects.create(nome='Fornecedor 1')
        fornecedor2 = Fornecedor.objects.create(nome='Fornecedor 2')
        
        # Cria um arquivo temporário para simular o upload de uma imagem
        imagem_temp = SimpleUploadedFile("produto_imagem.jpg", b"file_content", content_type="image/jpeg")
        imagem_temp2 = SimpleUploadedFile("produto_imagem.jpg", b"file_content", content_type="image/jpeg")
        
        # Cria alguns produtos de exemplo
        Produto.objects.create(
            nome='Produto 1',
            descricao='Descrição do Produto 1',
            categoria=categoria,
            fornecedor=fornecedor,
            preco_compra=100.0,
            preco_venda=200.0,
            imagem=imagem_temp
        )
        
        Produto.objects.create(
            nome='Produto 2',
            descricao='Descrição do Produto 2',
            categoria=categoria2,
            fornecedor=fornecedor2,
            preco_compra=100.0,
            preco_venda=200.0,
            imagem=imagem_temp2
        )

    def test_listar_produtos(self):
        # Faz login com o usuário de teste
        self.client.login(username='testuser', password='testpass')

        # Obtém a URL reversa para a view 'listar_produtos'
        url = reverse('listar_produtos')

        # Envia uma requisição GET para a URL
        response = self.client.get(url)

        # Verifica se a resposta tem status code 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifica se o template correto foi usado para renderizar a resposta
        self.assertTemplateUsed(response, 'produtos/listar_produtos.html')

        # Verifica se os nomes dos produtos estão presentes no conteúdo da resposta
        self.assertContains(response, 'Produto 1')
        self.assertContains(response, 'Produto 2')      

class EditarProdutoTest(TestCase):        
    def setUp(self):
        # Criar objetos de teste (categoria, fornecedor, produto)
        self.categoria = Categoria.objects.create(nome='Categoria 1')
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor 1')
        self.produto = Produto.objects.create(
            nome='Produto 1',
            descricao='Descrição do Produto 1',
            categoria=self.categoria,
            fornecedor=self.fornecedor,
            preco_compra=Decimal('10.00'),
            preco_venda=Decimal('20.00')
        )
        # Criar um usuário para autenticação
        self.user = Usuario.objects.create_user(username='testuser', password='testpass')
    
    def test_editar_produto(self):
        # Autenticar o usuário
        self.client.login(username='testuser', password='testpass')
        
        # Dados atualizados do produto
        nome_atualizado = 'Produto Atualizado'
        descricao_atualizada = 'Descrição atualizada do produto'
        categoria_atualizada = Categoria.objects.create(nome='Categoria Atualizada')
        fornecedor_atualizado = Fornecedor.objects.create(nome='Fornecedor Atualizado')
        preco_compra_atualizado = Decimal('15.00')
        preco_venda_atualizado = Decimal('25.00')
        
        # Dados para upload de imagem
        imagem_atualizada = SimpleUploadedFile("image.jpg", b"file_content", content_type="image/jpeg")
        
        # URL de edição do produto
        url = reverse('editar_produto', args=[self.produto.id])
        
        # Dados do formulário para atualização do produto
        form_data = {
            'nome': nome_atualizado,
            'descricao': descricao_atualizada,
            'categoria': categoria_atualizada.id,
            'fornecedor': fornecedor_atualizado.id,
            'preco_compra': preco_compra_atualizado,
            'preco_venda': preco_venda_atualizado,
            'imagem': imagem_atualizada
        }
        
        # Enviar requisição POST para atualizar o produto
        response = self.client.post(url, data=form_data, format='multipart')
        
        # Verificar se o redirecionamento ocorreu corretamente
        self.assertRedirects(response, reverse('listar_produtos'))
        
        # Atualizar o objeto produto
        self.produto.refresh_from_db()
        
        # Verificar se os dados foram atualizados corretamente
        self.assertEqual(self.produto.nome, nome_atualizado)
        self.assertEqual(self.produto.descricao, descricao_atualizada)
        self.assertEqual(self.produto.categoria, categoria_atualizada)
        self.assertEqual(self.produto.fornecedor, fornecedor_atualizado)
        self.assertEqual(self.produto.preco_compra, preco_compra_atualizado)
        self.assertEqual(self.produto.preco_venda, preco_venda_atualizado)
        
        # Verificar se a imagem foi atualizada corretamente
        self.assertIsNotNone(self.produto.imagem)
        
        # Limpar a imagem após o teste
        self.produto.imagem.delete()

class ExcluirProdutoTest(TestCase):
    def setUp(self):
        # Cria um usuário de teste
        self.user = Usuario.objects.create_user(username='testuser', password='testpass')
        
        # Cria um produto de exemplo
        self.categoria = Categoria.objects.create(nome='Categoria 1')
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor 1')
        self.produto = Produto.objects.create(
            nome='Produto 1',
            descricao='Descrição do Produto 1',
            categoria=self.categoria,
            fornecedor=self.fornecedor,
            preco_compra=Decimal('50.00'),
            preco_venda=Decimal('100.00')
        )

    def test_excluir_produto(self):
        # Faz login com o usuário de teste
        self.client.login(username='testuser', password='testpass')

        # Obtém a URL reversa para a view 'excluir_produto' com o ID do produto
        url = reverse('excluir_produto', args=[self.produto.id])

        # Envia uma requisição POST para a URL
        response = self.client.post(url)

        # Verifica se a resposta redireciona para a view 'listar_produtos'
        self.assertRedirects(response, reverse('listar_produtos'))

        # Verifica se o produto foi excluído do banco de dados
        self.assertFalse(Produto.objects.filter(id=self.produto.id).exists())

