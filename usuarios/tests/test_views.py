import unittest
from django.test import TestCase, Client
from usuarios.models import Usuario, Funcionario, Fornecedor, Cliente, Endereco
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from decimal import Decimal
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404
from usuarios.views import cadastrar_cliente, listar_clientes, editar_cliente

class CadastroFuncionarioTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = Usuario.objects.create_user(username='renatak12', password='0212')
    
    def test_cadastro_funcionario_gerente(self):
        # Faz o login do usuário admin
        self.client.login(username='renatak12', password='0212')
        
        # Simula uma requisição POST para cadastrar um gerente
        response = self.client.post(reverse('cadastro_funcionario', args=['gerente']), {
            'username': 'gerente1',
            'cpf': '12345678900',
            'remuneracao': '5000',
            'email': 'gerente1@gmail.com',
            'password': 'senha321'
        })
        
        # Verifica se houve o redirecionamento para a página correta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('logado'))
        
        # Verifica se o usuário gerente foi criado corretamente
        usuario = Usuario.objects.get(email='gerente1@gmail.com')
        self.assertEqual(usuario.username, 'gerente1')
        self.assertEqual(usuario.cargo, 'gerente')
        self.assertTrue(usuario.is_staff)
        self.assertTrue(usuario.is_superuser)
        
        # Verifica se o funcionário associado ao usuário foi criado corretamente
        funcionario = Funcionario.objects.get(usuario=usuario)
        self.assertEqual(funcionario.nome, 'gerente1')
        self.assertEqual(funcionario.cpf, '12345678900')
        self.assertEqual(funcionario.remuneracao, Decimal('5000'))
        self.assertEqual(funcionario.email, 'gerente1@gmail.com')
    
    def test_cadastro_funcionario_vendedor(self):
        # Faz o login do usuário admin
        self.client.login(username='renatak12', password='0212')
        
        # Simula uma requisição POST para cadastrar um vendedor
        response = self.client.post(reverse('cadastro_funcionario', args=['vendedor']), {
            'username': 'Vitoria Santos',
            'cpf': '999.888.555-00',
            'remuneracao': '2000',
            'email': 'vitoria1@gmail.com',
            'password': 'senha321'
        })
        
        # Verifica se houve o redirecionamento para a página correta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('logado'))
        
        # Verifica se o usuário vendedor foi criado corretamente
        usuario = Usuario.objects.get(email='vitoria1@gmail.com')
        self.assertEqual(usuario.username, 'Vitoria Santos')
        self.assertEqual(usuario.cargo, 'vendedor')
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)
        
        # Verifica se o funcionário associado ao usuário foi criado corretamente
        funcionario = Funcionario.objects.get(usuario=usuario)
        self.assertEqual(funcionario.nome, 'Vitoria Santos')
        self.assertEqual(funcionario.cpf, '999.888.555-00')
        self.assertEqual(funcionario.remuneracao, Decimal('2000'))
        self.assertEqual(funcionario.email, 'vitoria1@gmail.com')
        
    def test_cadastrar_gerente_get(self):
        response = self.client.get(reverse('cadastrar_gerente'))
        
        # Verifica se a resposta é um código de status 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verifica se o template correto está sendo usado
        self.assertTemplateUsed(response, 'usuarios/cadastros/cadastro_gerente.html')

    
    def test_cadastrar_vendedor_get(self):
        response = self.client.get(reverse('cadastrar_vendedor'))
        
        # Verifica se a resposta é um código de status 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verifica se o template correto está sendo usado
        self.assertTemplateUsed(response, 'usuarios/cadastros/cadastro_vendedor.html')

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = Usuario.objects.create_user(username='vitoria@gmail.com', password='senha321')
    
    def test_login_view_post_success(self):
        response = self.client.post(reverse('login'), {
            'username': 'vitoria@gmail.com',
            'password': 'senha321'
        })
        
        # Verifica se a resposta é um redirecionamento para a página correta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('logado'))
        
        # Verifica se o usuário está logado
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_post_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'vitoria@gmail.com',
            'password': 'senha456'
        })
        
        # Verifica se a resposta é um código de status 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verifica se a mensagem de erro é exibida corretamente
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Credenciais inválidas. Por favor, tente novamente.')
        
        # Verifica se o usuário não está logado
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        
        # Verifica se a resposta é um código de status 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verifica se o template correto está sendo usado
        self.assertTemplateUsed(response, 'usuarios/registros/login.html')

class LogadoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_logado_view(self):
        response = self.client.get(reverse('logado'))
        
        # Verifica se a resposta é um código de status 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verifica se o template correto está sendo usado
        self.assertTemplateUsed(response, 'usuarios/registros/logado.html')

class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = Usuario.objects.create_user(username='usuario1', password='senha123')
    
    def test_logout_view(self):
        # Faz o login do usuário antes de fazer o logout
        self.client.login(username='vitoria@gmail.com', password='senha321')
        
        response = self.client.get(reverse('logout'))
        
        # Verifica se houve o redirecionamento para a página correta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('homepage'))
        
        # Verifica se o usuário foi deslogado corretamente
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    
class ListarFuncionariosTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario1 = Usuario.objects.create(username='vitoria1@gmail.com', password='senha321')
        self.usuario2 = Usuario.objects.create(username='maria@gmail.com', password='senha321')
        self.funcionario1 = Funcionario.objects.create(nome='Vitoria Santos', cpf='99988855500', remuneracao='2000', email='vitoria1@gmail.com', usuario=self.usuario1)
        self.funcionario2 = Funcionario.objects.create(nome='Maria Ana', cpf='999.999.999-00', remuneracao='2000', email='maria@gmail.com', usuario=self.usuario2)
    
    def test_listar_funcionarios(self):
        response = self.client.get(reverse('listar_funcionarios'))
        
        # Verifica se a resposta é um código de status 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Verifica se o template correto está sendo usado
        self.assertTemplateUsed(response, 'usuarios/cadastros/listar_funcionarios.html')
        
        # Verifica se os funcionários estão sendo passados para o template corretamente
        funcionarios = response.context['funcionarios']
        self.assertEqual(len(funcionarios), 2)
        self.assertIn(self.funcionario1, funcionarios)
        self.assertIn(self.funcionario2, funcionarios)

class EditarFuncionarioTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = Usuario.objects.create_user(username='admin', password='admin123')
        self.funcionario = Funcionario.objects.create(nome='Funcionario', cpf='123456789', remuneracao='5000', email='funcionario@example.com', usuario=self.usuario)
    
    def test_editar_funcionario(self):
        # Faz o login do usuário admin
        self.client.login(username='renatak12', password='0212')
        
        # Simula uma requisição POST com dados atualizados
        response = self.client.post(reverse('editar_funcionario', args=[self.funcionario.id]), {
            'nome': 'Carlos',
            'cpf': '98765432100',
            'remuneracao': '2000',
            'email': 'carlos@gmail.com'
        })
        
        # Verifica se houve o redirecionamento para a página correta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_funcionarios'))
        
        # Atualiza o objeto do funcionário a partir do banco de dados
        funcionario_atualizado = get_object_or_404(Funcionario, id=self.funcionario.id)
        
        # Verifica se os dados do funcionário foram atualizados corretamente
        self.assertEqual(funcionario_atualizado.nome, 'Carlos')
        self.assertEqual(funcionario_atualizado.cpf, '98765432100')
        self.assertEqual(funcionario_atualizado.remuneracao, Decimal('2000'))
        self.assertEqual(funcionario_atualizado.email, 'carlos@gmail.com')

class DeletarFuncionarioTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = Usuario.objects.create_user(username='renatak12', password='0212')
        self.funcionario = Funcionario.objects.create(nome='Maria Ana', cpf='999.999.999-00', remuneracao='2000', email='maria@gmail.com', usuario=self.usuario)
    
    def test_deletar_funcionario(self):
        # Faz o login do usuário admin
        self.client.login(username='renatak12', password='0212')
        
        # Simula uma requisição POST para deletar o funcionário
        response = self.client.post(reverse('deletar_funcionario', args=[self.funcionario.id]))
        
        # Verifica se houve o redirecionamento para a página correta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_funcionarios'))
        
        # Verifica se o funcionário foi removido corretamente do banco de dados
        with self.assertRaises(Funcionario.DoesNotExist):
            funcionario_deletado = Funcionario.objects.get(id=self.funcionario.id)

class FornecedorViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_cadastrar_fornecedor_post(self):
        # Simula uma requisição POST para cadastrar um fornecedor
        response = self.client.post(reverse('cadastrar_fornecedor'), {
            'nome': 'Fornecedor1',
            'telefone': '12345678911',
            'cnpj': '12345678901234',
            'email': 'fornecedor1@gmail.com',
        })
        
        # Verifica se houve o redirecionamento para a página correta
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar_fornecedores'))
        
        # Verifica se o fornecedor foi criado corretamente
        fornecedor = Fornecedor.objects.get(nome='Fornecedor1')
        self.assertEqual(fornecedor.telefone, '12345678911')
        self.assertEqual(fornecedor.cnpj, '12345678901234')
        self.assertEqual(fornecedor.email, 'fornecedor1@gmail.com')
    
    def test_cadastrar_fornecedor_get(self):
        # Simula uma requisição GET para exibir o formulário de cadastro de fornecedor
        response = self.client.get(reverse('cadastrar_fornecedor'))
        
        # Verifica se a página de cadastro de fornecedor foi exibida corretamente
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fornecedor/cadastro_fornecedor.html')

    
    def test_listar_fornecedores(self):
        # Cria alguns fornecedores para testar a listagem
        Fornecedor.objects.create(nome='Fornecedor1', telefone='123456789', cnpj='12345678901234', email='fornecedor1@gmail.com')
        Fornecedor.objects.create(nome='Fornecedor2', telefone='987654321', cnpj='56789012345678', email='fornecedor2@gmail.com')
        
        # Simula uma requisição GET para listar os fornecedores
        response = self.client.get(reverse('listar_fornecedores'))
        
        # Verifica se a página foi exibida corretamente
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fornecedor/listar_fornecedores.html')
        
        # Verifica se os fornecedores foram listados corretamente
        fornecedores = response.context['fornecedores']
        self.assertEqual(len(fornecedores), 2)
        
        fornecedor1 = fornecedores[0]
        self.assertEqual(fornecedor1.nome, 'Fornecedor1')
        self.assertEqual(fornecedor1.telefone, '123456789')
        self.assertEqual(fornecedor1.cnpj, '12345678901234')
        self.assertEqual(fornecedor1.email, 'fornecedor1@gmail.com')
        
        fornecedor2 = fornecedores[1]
        self.assertEqual(fornecedor2.nome, 'Fornecedor2')
        self.assertEqual(fornecedor2.telefone, '987654321')
        self.assertEqual(fornecedor2.cnpj, '56789012345678')
        self.assertEqual(fornecedor2.email, 'fornecedor2@gmail.com')

    
    def test_editar_fornecedor(self):
        # Cria um fornecedor para testar a edição
        fornecedor = Fornecedor.objects.create(nome='Fornecedor3', telefone='123456789', cnpj='12345678901234', email='fornecedor3@gmail.com')
        
        # Define os dados a serem atualizados
        novo_nome = 'Novo Fornecedor'
        novo_cnpj = '98765432109876'
        novo_telefone = '987654321'
        novo_email = 'novo_fornecedor@gmail.com'
        
        # Define a URL para editar o fornecedor
        url = reverse('editar_fornecedor', args=[fornecedor.id])
        
        # Simula uma requisição POST para atualizar o fornecedor
        response = self.client.post(url, {
            'nome': novo_nome,
            'cnpj': novo_cnpj,
            'telefone': novo_telefone,
            'email': novo_email
        })
        
        # Verifica se o fornecedor foi atualizado corretamente
        fornecedor_atualizado = Fornecedor.objects.get(id=fornecedor.id)
        self.assertEqual(fornecedor_atualizado.nome, novo_nome)
        self.assertEqual(fornecedor_atualizado.cnpj, novo_cnpj)
        self.assertEqual(fornecedor_atualizado.telefone, novo_telefone)
        self.assertEqual(fornecedor_atualizado.email, novo_email)
        
        # Verifica se o redirecionamento ocorreu corretamente
        self.assertRedirects(response, reverse('listar_fornecedores'))

    
    def test_deletar_fornecedor(self):
        # Cria um fornecedor para testar a exclusão
        fornecedor = Fornecedor.objects.create(nome='Fornecedor1', telefone='123456789', cnpj='12345678901234', email='fornecedor1@gmail.com')
        
        # Define a URL para deletar o fornecedor
        url = reverse('deletar_fornecedor', args=[fornecedor.id])
        
        # Simula uma requisição POST para deletar o fornecedor
        response = self.client.post(url)
        
        # Verifica se o fornecedor foi excluído do banco de dados
        fornecedores = Fornecedor.objects.filter(id=fornecedor.id)
        self.assertFalse(fornecedores.exists())
        
        # Verifica se o redirecionamento ocorreu corretamente
        self.assertRedirects(response, reverse('listar_fornecedores'))


class CadastrarClienteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('cadastrar_cliente')
        self.estados = Endereco.get_estados_brasileiros()

    def test_cadastrar_cliente_post(self):
        data = {
            'nome': 'Cliente Teste',
            'cpf': '12345678900',
            'telefone': '999999999',
            'email': 'cliente@teste.com',
            'rua': 'Rua Teste',
            'numero': '123',
            'cidade': 'Cidade Teste',
            'estado': 'RN'
        }
        response = self.client.post(self.url, data)
        
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        self.assertEqual(Cliente.objects.count(), 1)
        cliente = Cliente.objects.first()
        self.assertEqual(cliente.nome, 'Cliente Teste')
        self.assertEqual(cliente.cpf, '12345678900')
        self.assertEqual(cliente.telefone, '999999999')
        self.assertEqual(cliente.email, 'cliente@teste.com')
        self.assertEqual(cliente.endereco.rua, 'Rua Teste')
        self.assertEqual(cliente.endereco.numero, '123')
        self.assertEqual(cliente.endereco.cidade, 'Cidade Teste')
        self.assertEqual(cliente.endereco.estado, 'RN')

    def test_cadastrar_cliente_get(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)  # Sucesso
        self.assertTemplateUsed(response, 'cliente/cadastro_cliente.html')
        self.assertIn('estados', response.context)
        estados_context = response.context['estados']
        self.assertEqual(estados_context, self.estados)

class ListarClientesTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('listar_clientes')

    def test_listar_clientes(self):
        # Cria alguns clientes de exemplo
        endereco1 = Endereco.objects.create(rua='Rua Teste', numero='123', cidade='Cidade Teste', estado='SP')
        endereco2 = Endereco.objects.create(rua='Rua Teste2', numero='321', cidade='Cidade Teste', estado='RN')
        Cliente.objects.create(nome='Cliente 1', cpf='12345678900', telefone='999999999', email='cliente1@teste.com', endereco=endereco1)
        Cliente.objects.create(nome='Cliente 2', cpf='98765432100', telefone='888888888', email='cliente2@teste.com', endereco=endereco2)

        response = self.client.get(reverse('listar_clientes'))
        
        self.assertEqual(response.status_code, 200)  # Sucesso
        self.assertTemplateUsed(response, 'cliente/listar_clientes.html')
        self.assertIn('clientes', response.context)
        clientes_context = response.context['clientes']
        self.assertEqual(clientes_context.count(), 2)

        # Verifica se os nomes dos clientes estão presentes na resposta
        self.assertContains(response, 'Cliente 1')
        self.assertContains(response, 'Cliente 2')
    
class EditarClienteTest(TestCase):
    def setUp(self):
        endereco = Endereco.objects.create(rua='Rua Teste', numero='123', cidade='Cidade Teste', estado='XX')
        self.cliente = Cliente.objects.create(nome='Cliente 1', cpf='12345678900', telefone='999999999', email='cliente1@teste.com', endereco=endereco)

    def test_editar_cliente(self):
        # Preparação
        cliente_id = self.cliente.id
        data = {
            'nome': 'Cliente Editado',
            'cpf': '98765432100',
            'telefone': '888888888',
            'email': 'cliente_editado@teste.com',
            'rua': 'Rua Editada',
            'numero': '456',
            'cidade': 'Cidade Editada',
            'estado': 'YY'
        }

        # Execução
        url = reverse('editar_cliente', kwargs={'cliente_id': cliente_id})
        response = self.client.post(url, data=data, follow=True)

        # Verificação
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cliente/listar_clientes.html')

        # Verificar se o cliente foi atualizado corretamente
        cliente_atualizado = get_object_or_404(Cliente, id=cliente_id)
        self.assertEqual(cliente_atualizado.nome, 'Cliente Editado')
        self.assertEqual(cliente_atualizado.cpf, '98765432100')
        self.assertEqual(cliente_atualizado.telefone, '888888888')
        self.assertEqual(cliente_atualizado.email, 'cliente_editado@teste.com')
        self.assertEqual(cliente_atualizado.endereco.rua, 'Rua Editada')
        self.assertEqual(cliente_atualizado.endereco.numero, '456')
        self.assertEqual(cliente_atualizado.endereco.cidade, 'Cidade Editada')
        self.assertEqual(cliente_atualizado.endereco.estado, 'YY')

class DeletarClienteTest(TestCase):
    def setUp(self):
        endereco = Endereco.objects.create(rua='Rua Teste', numero='123', cidade='Cidade Teste', estado='XX')
        self.cliente = Cliente.objects.create(nome='Cliente 1', cpf='12345678900', telefone='999999999', email='cliente1@teste.com', endereco=endereco)

    #def test_deletar_cliente(self):
    #    # Preparação
    #    cliente_id = self.cliente.id
    #
    #    # Execução
    #    url = reverse('deletar_cliente', kwargs={'cliente_id': cliente_id})
    #    response = self.client.post(url, follow=True)

        # Verificação
    #    self.assertRedirects(response, reverse('listar_clientes'))

        # Verificar se o cliente foi excluído corretamente
    #    cliente_excluido = get_object_or_404(Cliente, id=cliente_id)
    #    with self.assertRaises(Cliente.DoesNotExist):
    #        cliente_excluido.refresh_from_db()

