from django.test import TestCase
from accounts.models import Usuario , Fornecedor , Cliente, Endereco

class UsuarioTest(TestCase):
    def setUp(self):
        self.user = Usuario.objects.create_user(username='testuser', email='test@example.com', password='testpassword', nome='Test User')

    def test_primeiro_nome(self):

        self.assertEqual(self.user.primeiro_nome(), 'Test')

class FornecedorTest(TestCase):
    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor Teste', telefone='(11) 98765-4321', cnpj='12345678901234', email='fornecedor@teste.com')

    def test_primeiro_nome(self):
        self.assertEqual(self.fornecedor.primeiro_nome(), 'Fornecedor')

class ClienteTest(TestCase):
    def setUp(self):
        endereco = Endereco.objects.create(
            logradouro='Rua das Flores',
            numero='123',
            cep='12345-678',
            cidade='Cidade Teste',
            estado='Estado Teste'
        )

        self.cliente = Cliente.objects.create(
            nome='Fulano de Tal',
            telefone='(11) 98765-4321',
            cpf='123.456.789-00',
            email='fulano@example.com',
            endereco=endereco
        )

    def test_primeiro_nome(self):
        primeiro_nome_esperado = 'Fulano'
        self.assertEqual(self.cliente.primeiro_nome(), primeiro_nome_esperado)