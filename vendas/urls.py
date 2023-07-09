from django.urls import path
from . import views

urlpatterns = [
    
    path('categoria/cadastrar', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('categorias/listar', views.listar_categorias, name='listar_categorias'),
    path('categoria/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/excluir/<int:categoria_id>/', views.excluir_categoria, name='excluir_categoria'),

    path('compras/nova/', views.nova_compra, name='nova_compra'),
    path('compra/listar/', views.listar_compras, name='listar_compras'),
    path('compras/detalhar/<int:compra_id>/', views.detalhar_compra, name='detalhar_compra'),
    path('compras/excluir/<int:compra_id>/', views.excluir_compra, name='excluir_compra'),
    
    
    path('produto/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('produtos/listar/', views.listar_produtos, name='listar_produtos'),
    path('produto/detalhar/<int:produto_id>/', views.detalhar_produto, name='detalhar_produto'),
    path('produto/editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('produto/excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
    
    path('estoque/entrada/<int:produto_id>/', views.registrar_entrada, name='registrar_entrada'),
    path('estoque/saida/<int:produto_id>/', views.registrar_saida, name='registrar_saida'),
]
    
    
    
    
    
    
