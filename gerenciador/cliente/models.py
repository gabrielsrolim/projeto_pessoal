from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=40)
    endereco = models.CharField(max_length=200)

class Venda(models.Model):
    id_venda = models.AutoField(primary_key=True)
    data_compra = models.DateField()
    valor = models.DecimalField(max_digits=19,decimal_places=2)
    metragem = models.IntegerField()
    preco_unidade = models.DecimalField(max_digits=19,decimal_places=2)
    id_produto = models.ForeignKey('Produto')
    id_cliente = models.ForeignKey('Cliente')
    
class Produto(models.Model):
    id_produto = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    preco_compra = models.DecimalField(max_digits=19,decimal_places=2)
    preco_venda = models.DecimalField(max_digits=19,decimal_places=2)
    
class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    id_produto_fornecedor = models.ForeignKey('Produto')
    
class ComprasFornecedor(models.Model):
    id_compra_fornecedor = models.AutoField(primary_key=True)
    data_compra = models.DateField()
    metros_comprados = models.DecimalField(max_digits=19,decimal_places=2)
    valor_da_compra = models.DecimalField(max_digits=19,decimal_places=2)
    id_fornecedor = models.ForeignKey('Fornecedor')
    
class Stock(models.Model):
    id_stock = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=19,decimal_places=2)
    compra = models.BooleanField()
    data = models.DateField()
    id_compra_fornecedor = models.ForeignKey('ComprasFornecedor')
    id_venda = models.ForeignKey('Venda')
