from django.db import models
from django.contrib.auth.models import AbstractUser


class Endereco(models.Model):
    ESTADO_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    
    def __str__(self):
        return f"{self.estado}"


class Usuario(AbstractUser):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=15, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    imagem = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    endereco = models.OneToOneField(
        Endereco,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    email = models.EmailField(unique=True)
    
    def primeiro_nome(self):
        split_nome = self.nome.split(' ')
        return split_nome[0]


class Material(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
    
class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
        
    def primeiro_nome(self):
        split_nome = self.nome.split(' ')
        return split_nome[0] 


class Compra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.material.nome
      
    
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    estoque = models.PositiveIntegerField(default=0)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome



