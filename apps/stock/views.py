from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from .models import Categoria, Produto, Venda
from .models import Fornecedor, Cliente
from django.db import transaction
from decimal import Decimal


@method_decorator(login_required, name='dispatch')
class CriarCategoria(View):
    template_name = 'stock/categorias/criar.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        nome = request.POST.get('nome')

        # Cria a categoria com os dados recebidos do formulário
        Categoria.objects.create(nome=nome)
        messages.success(request, 'Categoria criada com sucesso!')
        return redirect('stock:criar_categoria')

@method_decorator(login_required, name='dispatch')
class ListarCategorias(View):
    template_name = 'stock/categorias/listar.html'

    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, self.template_name, {'categorias': categorias})
    
@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class ListarProdutos(View):
    template_name = 'stock/produtos/listar.html'

    def get(self, request):
        produtos = Produto.objects.all()
        return render(request, self.template_name, {'produtos': produtos})

@method_decorator(login_required, name='dispatch')
class EditarProduto(View):
    template_name = 'stock/produtos/editar.html'

    def get(self, request, produto_id):
        produto = get_object_or_404(Produto, id=produto_id)
        categorias = Categoria.objects.all()
        fornecedores = Fornecedor.objects.all()
        return render(request, self.template_name, {'produto': produto, 'categorias': categorias, 'fornecedores': fornecedores})

    def post(self, request, produto_id):
        produto = get_object_or_404(Produto, id=produto_id)
        categoria_id = request.POST.get('categoria')
        fornecedor_id = request.POST.get('fornecedor')

        # Atualiza os dados do produto com os valores recebidos do formulário
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco')
        produto.quantidade_estoque = request.POST.get('quantidade_estoque')
        produto.categoria_id = categoria_id
        produto.fornecedor_id = fornecedor_id

        imagem = request.FILES.get('imagem')
        if imagem:
            produto.imagem = imagem

        produto.save()

        return redirect('stock:listar_produtos')

@method_decorator(login_required, name='dispatch')
class ExcluirProduto(View):
    template_name = 'stock/produtos/excluir.html'

    def get(self, request, produto_id):
        produto = get_object_or_404(Produto, id=produto_id)
        return render(request, self.template_name, {'produto': produto})

    def post(self, request, produto_id):
        produto = get_object_or_404(Produto, id=produto_id)
        produto.delete()
        return redirect('stock:listar_produtos')
    
#============================================================
# VIEWS ESTOQUE
@method_decorator(login_required, name='dispatch')
class AdicionarEstoque(View):
    template_name = 'stock/adicionar.html'

    def get(self, request, produto_id):
        produto = get_object_or_404(Produto, id=produto_id)
        return render(request, self.template_name, {'produto': produto})

    def post(self, request, produto_id):
        produto = get_object_or_404(Produto, id=produto_id)
        quantidade_adicionada = request.POST.get('quantidade')
        
        if quantidade_adicionada and quantidade_adicionada.isdigit():
            quantidade_adicionada = int(quantidade_adicionada)
            produto.quantidade_estoque = quantidade_adicionada
            produto.save()

        return redirect('stock:listar_estoque')

@method_decorator(login_required, name='dispatch')
class ListarEstoque(View):
    template_name = 'stock/listar.html'

    def get(self, request):
        produtos = Produto.objects.all()
        return render(request, self.template_name, {'produtos': produtos})
    
    
#=====================================================
# VIEWS VENDA

@method_decorator(login_required, name='dispatch')
class RealizarVenda(View):
    template_name = 'stock/vendas/realizar.html'

    def get(self, request):
        clientes = Cliente.objects.all()
        produtos = Produto.objects.all()
        return render(request, self.template_name, {'clientes': clientes, 'produtos': produtos})

    def post(self, request):
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = int(request.POST.get('quantidade', 0))
        #parcelamento = int(request.POST.get('parcelamento', 1))

        cliente = get_object_or_404(Cliente, id=cliente_id)
        #produto = get_object_or_404(Produto, id=produto_id)
        
        produto = get_object_or_404(Produto, id=produto_id)
        if produto.quantidade_estoque < quantidade:
            # Caso a quantidade disponível seja insuficiente, exiba uma mensagem de erro
            messages.error(request, "Quantidade insuficiente em estoque.")
            return redirect('stock:realizar_venda')
        
        preco = Decimal(produto.preco)
        valor_total = quantidade * preco
        
        forma_pagamento = request.POST.get('forma_pagamento')
        parcelamento = int(request.POST.get('parcelamento', 1))

        if forma_pagamento in ["dinheiro", "pix", "debito"]:
            desconto = Decimal('0.1')  # 10% de desconto
            valor_total_compra = valor_total * (1 - desconto)
            if parcelamento > 1:
                valor_parcela = valor_total_compra / parcelamento
            else:
                valor_parcela = valor_total_compra
        elif forma_pagamento == "cartao_credito" and parcelamento > 6:
            juros = Decimal('0.03')  # 3% de juros para parcelamento maior que 6x
            valor_total_compra = valor_total * (1 + juros)
            valor_parcela = valor_total_compra / parcelamento
        else:
            valor_total_compra = valor_total
            valor_parcela = valor_total_compra

        venda = Venda(
            cliente=cliente,
            produto=produto,
            quantidade=quantidade,
            preco=preco,
            forma_pagamento=forma_pagamento,
            parcelamento=parcelamento,
            valor_total=valor_total,
            valor_parcela=valor_parcela,
            valor_total_compra=valor_total_compra,
            desconto=desconto if forma_pagamento in ["dinheiro", "pix", "debito"] else 0,
        )
        venda.save()
        
        with transaction.atomic():
            produto.quantidade_estoque -= quantidade
            produto.save()

        return redirect('stock:listar_vendas')
    

@method_decorator(login_required, name='dispatch')
class ListarVendas(View):
    template_name = 'stock/vendas/listar.html'

    def get(self, request):
        vendas = Venda.objects.all()
        return render(request, self.template_name, {'vendas': vendas})
    
    
@method_decorator(login_required, name='dispatch')   
class ExcluirVenda(View):
    template_name = 'stock/vendas/excluir.html'

    def get(self, request, venda_id):
        venda = get_object_or_404(Venda, id=venda_id)
        return render(request, self.template_name, {'venda': venda})

    def post(self, request, venda_id):
        venda = get_object_or_404(Venda, id=venda_id)

        with transaction.atomic():
            # Restaurar a quantidade do produto no estoque
            produto = venda.produto
            produto.quantidade_estoque += venda.quantidade
            produto.save()

            # Excluir a venda
            venda.delete()

            # Exibir mensagem de sucesso
            messages.success(request, 'Venda excluída com sucesso.')

        return redirect('stock:listar_vendas')

class DetalharVenda(View):
    template_name = 'stock/vendas/detalhar.html'

    def get(self, request, venda_id):
        venda = get_object_or_404(Venda, id=venda_id)
        return render(request, self.template_name, {'venda': venda})
    
    
