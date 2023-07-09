import unittest
from django.test import TestCase, Client
from usuarios.models import Usuario, Funcionario, Fornecedor, Cliente , Endereco
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from decimal import Decimal
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404


class TestUsuarioModel(TestCase):
    def setUp(self):
        Usuario.objects.create_user(username='Vitoria Santos', password='senha321')

    def test_nome_usuario(self):
        usuario = Usuario.objects.get(id=1)
        self.assertEqual(usuario.username, 'Vitoria Santos')

    def test_senha_usuario(self):
        usuario = Usuario.objects.get(id=1)
        self.assertTrue(usuario.check_password('senha321'))

    def test_administrador_usuario(self):
        usuario = Usuario.objects.get(id=1)
        self.assertFalse(usuario.is_superuser)

class UsuarioTest(TestCase):
    def test_criar_usuario(self):
        # Cria um usuário com cargo de gerente
        usuario_gerente = Usuario.objects.create_user(username='gerente1', password='senha123', cargo='gerente')
        
        # Verifica se o usuário foi criado corretamente
        self.assertEqual(usuario_gerente.username, 'gerente1')
        self.assertTrue(usuario_gerente.check_password('senha123'))
        self.assertEqual(usuario_gerente.cargo, 'gerente')
        
        # Cria um usuário com cargo de vendedor
        usuario_vendedor = Usuario.objects.create_user(username='vendedor1', password='senha456', cargo='vendedor')
        
        # Verifica se o usuário foi criado corretamente
        self.assertEqual(usuario_vendedor.username, 'vendedor1')
        self.assertTrue(usuario_vendedor.check_password('senha456'))
        self.assertEqual(usuario_vendedor.cargo, 'vendedor')

class FuncionarioTest(TestCase):
    def setUp(self):
        # Cria um usuário para associar ao funcionário
        self.usuario = Usuario.objects.create_user(username='gerente1', password='senha321', cargo='gerente')

    def test_formatar_cpf(self):
        # Cria um funcionário
        funcionario = Funcionario.objects.create(
            nome='João',
            cpf='12345678901',
            remuneracao=5000.00,
            email='joao@gmail.com',
            usuario=self.usuario
        )
        
        # Verifica se o CPF foi formatado corretamente
        cpf_formatado = funcionario.formatar_cpf()
        self.assertEqual(cpf_formatado, '123.456.789-01')
        
    def test_str(self):
        # Cria um funcionário
        funcionario = Funcionario.objects.create(
            nome='Maria',
            cpf='98765432109',
            remuneracao=4000.00,
            email='maria@example.com',
            usuario=self.usuario
        )
        
        # Verifica se a representação em string do funcionário está correta
        str_funcionario = str(funcionario)
        self.assertEqual(str_funcionario, 'Maria gerente')

class FornecedorTest(TestCase):
    def setUp(self):
        self.fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            telefone='11999999999',
            cnpj='12345678901234',
            email='fornecedor@gmail.com'
        )

    def test_str(self):
        str_fornecedor = str(self.fornecedor)
        self.assertEqual(str_fornecedor, 'Fornecedor Teste')

class EnderecoTest(TestCase):
    def setUp(self):
        self.endereco = Endereco.objects.create(
            rua='Rua Teste',
            numero='123',
            cidade='Cidade Teste',
            estado='RN'
        )

    def test_str(self):
        str_endereco = str(self.endereco)
        self.assertEqual(str_endereco, 'Rua Teste, 123, Cidade Teste/RN')

    def test_get_estados_brasileiros(self):
        estados = Endereco.get_estados_brasileiros()
        self.assertEqual(len(estados), 27)  # Check if the number of states is correct
        self.assertEqual(estados[0], ('AC', 'Acre'))  # Check if the first state is correct
        self.assertEqual(estados[26], ('TO', 'Tocantins'))  # Check if the last state is correct


class ClienteTest(TestCase):
    def setUp(self):
        self.endereco = Endereco.objects.create(
            rua='Rua Teste',
            numero='123',
            cidade='Cidade Teste',
            estado='RN'
        )
        self.cliente = Cliente.objects.create(
            nome='Cliente Teste',
            endereco=self.endereco,
            telefone='999999999',
            cpf='12345678900',
            email='cliente@gmail.com'
        )

    def test_str(self):
        str_cliente = str(self.cliente)
        self.assertEqual(str_cliente, 'Cliente Teste')

