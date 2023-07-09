from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    CARGO_CHOICES = [
        ('gerente', 'Gerente'),
        ('vendedor', 'Vendedor'),
    ]
    cargo = models.CharField(max_length=255, choices=CARGO_CHOICES, null=False, blank=False)

class Funcionario(models.Model):   
    nome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False, blank=False)
    remuneracao = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def formatar_cpf(self):
        cpf_formatado = f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        return cpf_formatado
    # Error corrigido no FuncionarioTest
    def __str__(self):
        return f"{self.nome} {self.usuario.cargo}"
       
class Fornecedor(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    cnpj = models.CharField(max_length=18, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    
    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua = models.CharField(max_length=255, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    cidade = models.CharField(max_length=255, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False)
    
    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.cidade}/{self.estado}"
    
    @staticmethod
    def get_estados_brasileiros():
        estados = [
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
            ('TO', 'Tocantins')
        ]
        return estados
    
class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    
    def __str__(self):
        return self.nome
    

