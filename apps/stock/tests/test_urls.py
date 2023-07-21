from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from stock.views import (
    CriarCategoria, ListarCategorias, EditarCategoria, ExcluirCategoria,
    CriarProduto, ListarProdutos, EditarProduto, ExcluirProduto
)

class TestUrls(SimpleTestCase):
    def test_criar_categoria_url_resolves(self):
        url = reverse('stock:criar_categoria')
        self.assertEqual(resolve(url).func.view_class, CriarCategoria)

    def test_listar_categorias_url_resolves(self):
        url = reverse('stock:listar_categorias')
        self.assertEqual(resolve(url).func.view_class, ListarCategorias)

    def test_editar_categoria_url_resolves(self):
        url = reverse('stock:editar_categoria', args=['1'])  
        self.assertEqual(resolve(url).func.view_class, EditarCategoria)

    def test_excluir_categoria_url_resolves(self):
        url = reverse('stock:excluir_categoria', args=['1'])  
        self.assertEqual(resolve(url).func.view_class, ExcluirCategoria)

    def test_criar_produto_url_resolves(self):
        url = reverse('stock:criar_produto')
        self.assertEqual(resolve(url).func.view_class, CriarProduto)

    def test_listar_produtos_url_resolves(self):
        url = reverse('stock:listar_produtos')
        self.assertEqual(resolve(url).func.view_class, ListarProdutos)

    def test_editar_produto_url_resolves(self):
        url = reverse('stock:editar_produto', args=['1'])  # Substitua '1' pelo ID do produto
        self.assertEqual(resolve(url).func.view_class, EditarProduto)

    def test_excluir_produto_url_resolves(self):
        url = reverse('stock:excluir_produto', args=['1'])  # Substitua '1' pelo ID do produto
        self.assertEqual(resolve(url).func.view_class, ExcluirProduto)

