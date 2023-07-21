from django.test import TestCase
from stock.models import Categoria, Produto

class CategoriaTest(TestCase):
    def test_str_method(self):
        categoria = Categoria.objects.create(nome='Categoria de Teste')

        self.assertEqual(str(categoria), 'Categoria de Teste')

class ProdutoTest(TestCase):
    def test_str_method(self):
        categoria = Categoria.objects.create(nome='Categoria de Teste')

        produto = Produto.objects.create(categoria=categoria, nome='Produto Teste', preco='100.00', quantidade_estoque='10')

        self.assertEqual(str(produto), 'Produto Teste')
