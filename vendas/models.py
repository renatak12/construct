from django.db import models
from usuarios.models import Usuario, Funcionario, Fornecedor, Cliente, Endereco
from django.db.models import Sum
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    preco_compra = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    
    def registrar_entrada_estoque(self, quantidade):
        estoque = Estoque.objects.get(produto=self)
        estoque.quantidade += quantidade
        estoque.save()

    def registrar_saida_estoque(self, quantidade):
        estoque = Estoque.objects.get(produto=self)
        if estoque.quantidade >= quantidade:
            estoque.quantidade -= quantidade
            estoque.save()
        else:
            raise Exception("Quantidade insuficiente no estoque.")

    def __str__(self):
        return self.nome
    
    
class Compra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    
    def relatorio_movimentacao_estoque(self, data_inicial, data_final):
        movimentacoes = []
        itens_compra = self.itenscompra.all()  
        
        for item_compra in itens_compra:
            movimentacao = {
                'produto': item_compra.produto,
                'quantidade': item_compra.quantidade,
                'data': self.data,
                'tipo': 'Entrada'
            }
            movimentacoes.append(movimentacao)

        return movimentacoes
        
    def __str__(self):
        return f"Compra realizada em: {self.data} - Fornecedor: {self.fornecedor.nome}"
    

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itenscompra')  # Corrigido o nome do relacionamento
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)  
    
    def calcular_subtotal(self):
        subtotal = self.produto.preco_venda * self.quantidade     
        return subtotal
    
    def save(self, *args, **kwargs):
        self.subtotal = self.calcular_subtotal()     
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.quantidade} - {self.subtotal}'
    
    
class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(null=False, blank=False)
    
    def __str__(self):
        return f"{self.produto.nome} - Quantidade: {self.quantidade_disponivel}"
    
class Venda(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda #{self.id}"
    
class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(null=False, blank=False)
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f"Item #{self.id} - Produto: {self.produto.nome}"

class Pagamento(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('credito', 'Crédito'),
        ('debito', 'Débito'),
        ('dinheiro', 'Dinheiro'),
    ]
    venda = models.OneToOneField(Venda, on_delete=models.CASCADE)
    forma_pagamento = models.CharField(max_length=255, choices=FORMA_PAGAMENTO_CHOICES)
    parcelas = models.PositiveIntegerField(null=True, blank=True)

    def calcular_valor_total(self):
        valor_total = self.venda.itemvenda_set.aggregate(Sum('preco_unitario'))['preco_unitario__sum']
        
        if self.forma_pagamento == 'credito':
            if self.parcelas and self.parcelas <= 6:
                valor_total *= 1.0  # Sem juros
            elif self.parcelas and self.parcelas == 10:
                valor_total *= 1.05  # Acréscimo de 5%
        
        if self.forma_pagamento in ['debito', 'dinheiro']:
            valor_total *= 0.9  # Desconto de 10%
        
        return valor_total

    def __str__(self):
        return f"Pagamento - Venda: {self.venda.id}"

class NotaFiscal(models.Model):
    venda = models.OneToOneField(Venda, on_delete=models.CASCADE)
    numero = models.CharField(max_length=255, null=False, blank=False)
    data_emissao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nota Fiscal - Venda: {self.venda.id}"