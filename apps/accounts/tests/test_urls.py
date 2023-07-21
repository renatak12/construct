from django.test import TestCase
from django.urls import reverse, resolve
from accounts import views

class TestUrls(TestCase):
    def test_login_url(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class, views.Login)

    def test_signup_url(self):
        url = reverse('accounts:signup')
        self.assertEqual(resolve(url).func.view_class, views.SignUp)

    def test_logado_url(self):
        url = reverse('accounts:logado')
        self.assertEqual(resolve(url).func.view_class, views.Logado)

    def test_logout_url(self):
        url = reverse('accounts:logout')
        self.assertEqual(resolve(url).func.view_class, views.Logout)

    def test_profile_url(self):
        url = reverse('accounts:profile')
        self.assertEqual(resolve(url).func.view_class, views.Profile)

    def test_upload_image_url(self):
        url = reverse('accounts:upload_image')
        self.assertEqual(resolve(url).func.view_class, views.UploadImageView)

    def test_remove_image_url(self):
        url = reverse('accounts:remove_image')
        self.assertEqual(resolve(url).func.view_class, views.RemoveImageView)

    def test_criar_fornecedor_url(self):
        url = reverse('accounts:criar_fornecedor')
        self.assertEqual(resolve(url).func.view_class, views.CriarFornecedor)

    def test_listar_fornecedor_url(self):
        url = reverse('accounts:listar_fornecedor')
        self.assertEqual(resolve(url).func.view_class, views.ListarFornecedor)

    def test_editar_fornecedor_url(self):
        url = reverse('accounts:editar_fornecedor', args=['1'])  
        self.assertEqual(resolve(url).func.view_class, views.EditarFornecedor)

    def test_excluir_fornecedor_url(self):
        url = reverse('accounts:excluir_fornecedor', args=['1'])  
        self.assertEqual(resolve(url).func.view_class, views.ExcluirFornecedor)

    def test_criar_cliente_url(self):
        url = reverse('accounts:criar_cliente')
        self.assertEqual(resolve(url).func.view_class, views.CriarCliente)

    def test_listar_clientes_url(self):
        url = reverse('accounts:listar_clientes')
        self.assertEqual(resolve(url).func.view_class, views.ListarClientes)

    def test_editar_cliente_url(self):
        url = reverse('accounts:editar_cliente', args=['1'])  
        self.assertEqual(resolve(url).func.view_class, views.EditarCliente)

    def test_excluir_cliente_url(self):
        url = reverse('accounts:excluir_cliente', args=['1'])  
        self.assertEqual(resolve(url).func.view_class, views.ExcluirCliente)
