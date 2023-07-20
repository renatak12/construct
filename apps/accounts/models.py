from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    nome = models.CharField(max_length=200, null=False)
    cpf = models.CharField(max_length=15, null=True)
    telefone = models.CharField(max_length=20, null=True)
    imagem = models.ImageField(upload_to='usuarios/', null=True)
    
    email = models.EmailField(unique=True)
    
    def primeiro_nome(self):
        split_nome = self.nome.split(' ')
        return split_nome[0]

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200, null=False)
    telefone = models.CharField(max_length=20, null=True)
    cnpj = models.CharField(max_length=15, null=True)
    
    email = models.EmailField(unique=True)
    
    def primeiro_nome(self):
        split_nome = self.nome.split(' ')
        return split_nome[0]
    
    
class Endereco(models.Model):
    logradouro = models.CharField(max_length=200, null=True)
    numero = models.CharField(max_length=10, null=True)
    cep = models.CharField(max_length=10, null=True)
    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=100, null=True)


class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=False)
    telefone = models.CharField(max_length=20, null=True)
    cpf = models.CharField(max_length=15, null=True)
    email = models.EmailField(unique=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)

    def primeiro_nome(self):
        split_nome = self.nome.split(' ')
        return split_nome[0]
