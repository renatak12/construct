from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logado/', views.Logado.as_view(), name='logado'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('upload/image/', views.UploadImageView.as_view(), name='upload_image'),
    path('remove/image/', views.RemoveImageView.as_view(), name='remove_image'),
    
    path('criar/fornecedor', views.CriarFornecedor.as_view(), name='criar_fornecedor'),
    path('listar/fornecedor', views.ListarFornecedor.as_view(), name='listar_fornecedor'),
    path('editar/<str:fornecedor_id>/fornecedores', views.EditarFornecedor.as_view(), name='editar_fornecedor'),
    path('excluir/<str:fornecedor_id>/fornecedor', views.ExcluirFornecedor.as_view(), name='excluir_fornecedor'),
    
    path('criar/cliente', views.CriarCliente.as_view(), name='criar_cliente'),
    path('listar/clientes', views.ListarClientes.as_view(), name='listar_clientes'),
    path('editar/<str:cliente_id>/cliente', views.EditarCliente.as_view(), name='editar_cliente'),
    path('excluir/<str:cliente_id>/cliente', views.ExcluirCliente.as_view(), name='excluir_cliente'),
]


