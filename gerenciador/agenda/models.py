from django.db import models

# Create your models here.

class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=40)
    endereco = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'pessoas'

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    pessoa = models.ForeignKey('Pessoa')
    
    class Meta:
        db_table = 'clientes'

class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    valor_unidade = models.DecimalField(max_digits=19,decimal_places=2)
    total_metros = models.DecimalField(max_digits=19,decimal_places=2)
    produto = models.ForeignKey('Produto')    
    pessoa = models.ForeignKey('Pessoa')

    class Meta:
        db_table = 'fornecedores'

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = 'produtos'


