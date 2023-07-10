from django.contrib import admin
from .models import Endereco, Usuario, Material, Fornecedor, Compra, Produto

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ['logradouro', 'numero', 'cidade', 'estado']
    list_filter = ['estado']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'telefone']
    search_fields = ['nome', 'cpf', 'telefone']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cnpj', 'telefone', 'email']
    search_fields = ['nome', 'cnpj', 'email']

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['fornecedor', 'material', 'quantidade', 'preco_custo', 'data_compra']
    list_filter = ['fornecedor', 'material']
    search_fields = ['fornecedor__nome', 'material__nome']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco_unitario', 'estoque', 'fornecedor', 'material']
    list_filter = ['fornecedor', 'material']
    search_fields = ['nome']





