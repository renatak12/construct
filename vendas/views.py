from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, Fornecedor, Compra, ItemCompra
from decimal import Decimal


def cadastrar_categoria(request):
    if request.method == 'POST':
        nome = request.POST['nome']

        categoria = Categoria(nome=nome)
        categoria.save()
        
        return redirect('listar_categorias')
    return render(request, 'categorias/cadastrar_categoria.html')


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar_categorias.html', {'categorias': categorias})


def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        nome = request.POST['nome']
        categoria.nome = nome
        categoria.save()
        return redirect('listar_categorias')
    
    return render(request, 'categorias/editar_categoria.html', {'categoria': categoria})


def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')

    return render(request, 'categorias/excluir_categoria.html', {'categoria': categoria})

def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        categoria_id = request.POST['categoria']
        fornecedor_id = request.POST['fornecedor']
        preco_compra = request.POST['preco_compra']
        preco_venda = request.POST['preco_venda']
        
        imagem = request.FILES.get('imagem')
        
        produto = Produto(
            nome=nome,
            descricao=descricao,
            categoria_id=categoria_id,
            fornecedor_id=fornecedor_id,
            preco_compra=preco_compra,
            preco_venda=preco_venda,
            imagem=imagem
        )
        produto.save()
        
        return redirect('listar_produtos')
    else:
        categorias = Categoria.objects.all()
        fornecedores = Fornecedor.objects.all()

        context = {
            'categorias': categorias,
            'fornecedores': fornecedores
        }
    
    return render(request, 'produtos/cadastrar_produto.html', context)

def detalhar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/detalhar_produto.html', {'produto': produto})

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        categoria_id = request.POST['categoria']
        fornecedor_id = request.POST['fornecedor']
        preco_compra = request.POST['preco_compra']
        preco_venda = request.POST['preco_venda']

        produto.nome = nome
        produto.descricao = descricao
        produto.categoria_id = categoria_id
        produto.fornecedor_id = fornecedor_id
        produto.preco_compra = preco_compra
        produto.preco_venda = preco_venda

        imagem = request.FILES.get('imagem')
        if imagem:
            produto.imagem = imagem

        produto.save()

        return redirect('listar_produtos')
    else:
        categorias = Categoria.objects.all()
        fornecedores = Fornecedor.objects.all()

        context = {
            'produto': produto,
            'categorias': categorias,
            'fornecedores': fornecedores
        }

    return render(request, 'produtos/editar_produto.html', context)


def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')

    return render(request, 'produtos/excluir_produto.html', {'produto': produto})


def registrar_entrada(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        quantidade = int(request.POST['quantidade'])
        produto.registrar_entrada_estoque(quantidade)
        return redirect('detalhes_produto', produto_id=produto_id)

    context = {'produto': produto}
    return render(request, 'estoque/registrar_entrada.html', context)


def registrar_saida(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        quantidade = int(request.POST['quantidade'])
        produto.registrar_saida_estoque(quantidade)
        return redirect('detalhes_produto', produto_id=produto_id)

    context = {'produto': produto}
    return render(request, 'estoque/registrar_saida.html', context)

def nova_compra(request):
    fornecedores = Fornecedor.objects.all()
    produtos = Produto.objects.all()

    if request.method == 'POST':
        fornecedor_id = request.POST['fornecedor']
        data = request.POST['data']
        itens_compra = []

        for produto in produtos:
            quantidade = int(request.POST.get(f'quantidade_{produto.id}', 0))
            if quantidade > 0:
                subtotal = Decimal(request.POST.get(f'subtotal_{produto.id}', 0))
                item_compra = ItemCompra(produto=produto, quantidade=quantidade, subtotal=subtotal)
                itens_compra.append(item_compra)

        if fornecedor_id and data and itens_compra:
            fornecedor = Fornecedor.objects.get(id=fornecedor_id)
            compra = Compra(fornecedor=fornecedor, data=data)
            compra.save()

            for item_compra in itens_compra:
                item_compra.compra = compra
                item_compra.save()

            return redirect('listar_compras')

    context = {
        'fornecedores': fornecedores,
        'produtos': produtos
    }

    return render(request, 'compras/nova_compra.html', context)


def listar_compras(request):
    compras = Compra.objects.all()
    
    context = {
        'compras': compras
    }
    
    return render(request, 'compras/listar_compras.html', context)


def excluir_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    
    if request.method == 'POST':
        compra.delete()
        return redirect('listar_compras')
    
    context = {'compra': compra}
    return render(request, 'compras/excluir_compra.html', context)


def detalhar_compra(request, compra_id):
    compra = get_object_or_404(Compra, id=compra_id)
    
    context = {
        'compra': compra
    }
    
    return render(request, 'compras/detalhar_compra.html', context)