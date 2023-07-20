from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Categoria
from .models import Produto, Fornecedor

class CriarCategoria(View):
    template_name = 'stock/categorias/criar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        nome = request.POST.get('nome')

        # Cria a categoria com os dados recebidos do formulário
        categoria = Categoria.objects.create(nome=nome)
        messages.success(request, 'Categoria criada com sucesso!')
        return redirect('stock:criar_categoria')

class ListarCategorias(View):
    template_name = 'stock/categorias/listar.html'

    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, self.template_name, {'categorias': categorias})
    

class EditarCategoria(View):
    template_name = 'stock/categorias/editar.html'

    def get(self, request, categoria_id):
        categoria = get_object_or_404(Categoria, id=categoria_id)
        return render(request, self.template_name, {'categoria': categoria})

    def post(self, request, categoria_id):
        categoria = get_object_or_404(Categoria, id=categoria_id)
        nome = request.POST.get('nome')

        # Atualiza os dados da categoria com os valores recebidos do formulário
        categoria.nome = nome
        categoria.save()

        messages.success(request, 'Categoria atualizada com sucesso!')
        return redirect('stock:listar_categorias')


class ExcluirCategoria(View):
    template_name = 'stock/categorias/excluir.html'

    def get(self, request, categoria_id):
        categoria = get_object_or_404(Categoria, id=categoria_id)
        return render(request, self.template_name, {'categoria': categoria})

    def post(self, request, categoria_id):
        categoria = get_object_or_404(Categoria, id=categoria_id)
        categoria.delete()
        messages.success(request, 'Categoria excluída com sucesso!')
        return redirect('stock:listar_categorias')


#=================================================================
# VIEWS PRODUTOS


class CriarProduto(View):
    template_name = 'stock/produtos/criar.html'

    def get(self, request):
        categorias = Categoria.objects.all()
        fornecedores = Fornecedor.objects.all()
        return render(request, self.template_name, {'categorias': categorias, 'fornecedores': fornecedores})

    def post(self, request):
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        quantidade_estoque = request.POST.get('quantidade_estoque')
        categoria_id = request.POST.get('categoria')
        fornecedor_id = request.POST.get('fornecedor')
        imagem = request.FILES.get('imagem')

        categoria = get_object_or_404(Categoria, id=categoria_id)
        fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)

        produto = Produto(nome=nome, descricao=descricao, preco=preco, quantidade_estoque=quantidade_estoque,
                          categoria=categoria, fornecedor=fornecedor, imagem=imagem)
        produto.save()

        return redirect('stock:criar_produto')

