from django.test import TestCase
from stock.models import Categoria, Produto , Cliente , Venda

class CategoriaTest(TestCase):
    def test_str_method(self):
        categoria = Categoria.objects.create(nome='Categoria de Teste')

        self.assertEqual(str(categoria), 'Categoria de Teste')

class ProdutoTest(TestCase):
    def test_str_method(self):
        categoria = Categoria.objects.create(nome='Categoria de Teste')

        produto = Produto.objects.create(categoria=categoria, nome='Produto Teste', preco='100.00', quantidade_estoque='10')

        self.assertEqual(str(produto), 'Produto Teste')

class VendaModelTest(TestCase):
    def setUp(self):
        # Create a test Categoria object
        self.categoria = Categoria.objects.create(nome="Test Category")

        # Create a test Cliente object
        self.cliente = Cliente.objects.create(nome="Test Customer", email="test@example.com")

        # Create a test Produto object
        self.produto = Produto.objects.create(nome="Test Product", preco=10.0, categoria=self.categoria)

        # Create a test Venda object
        self.venda = Venda.objects.create(
            cliente=self.cliente,
            produto=self.produto,
            quantidade=5,
            preco=10.0,
            forma_pagamento="Credit Card",
            parcelamento=3,
            valor_total=50.0,
            valor_parcela=16.67,
            valor_total_compra=50.0,
            desconto=0,
        )

    def test_venda_fields(self):
        # Verify the fields of the Venda object
        self.assertEqual(self.venda.cliente, self.cliente)
        self.assertEqual(self.venda.produto, self.produto)
        self.assertEqual(self.venda.quantidade, 5)
        self.assertEqual(self.venda.preco, 10.0)
        self.assertEqual(self.venda.forma_pagamento, "Credit Card")
        self.assertEqual(self.venda.parcelamento, 3)
        self.assertEqual(self.venda.valor_total, 50.0)
        self.assertEqual(self.venda.valor_parcela, 16.67)
        self.assertEqual(self.venda.valor_total_compra, 50.0)
        self.assertEqual(self.venda.desconto, 0)

    def test_venda_str_representation(self):
        # Verify the __str__ representation of the Venda object
        expected_str = f"{self.cliente.nome} - {self.produto} - Quantidade: 5"
        self.assertEqual(str(self.venda), expected_str)