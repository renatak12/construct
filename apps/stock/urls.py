from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    path('criar/categoria', views.CriarCategoria.as_view(), name='criar_categoria'),
    path('listar/categorias', views.ListarCategorias.as_view(), name='listar_categorias'),
    path('editar/<str:categoria_id>/categoria', views.EditarCategoria.as_view(), name='editar_categoria'),
    path('excluir/<str:categoria_id>/categoria', views.ExcluirCategoria.as_view(), name='excluir_categoria'),
    
    path('criar/produto', views.CriarProduto.as_view(), name='criar_produto'),
]
