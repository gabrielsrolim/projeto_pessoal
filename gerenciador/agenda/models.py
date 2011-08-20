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
    id_pessoa = models.ForeignKey('Pessoa')
    
    class Meta:
        db_table = 'clientes'

class Fornecedor(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    valor_unidade = models.DecimalField(max_digits=19,decimal_places=2)
    total_metros = models.DecimalField(max_digits=19,decimal_places=2)
    id_produto = models.ForeignKey('Produto')    
    id_pessoa = models.ForeignKey('Pessoa')

    class Meta:
        db_table = 'fornecedores'

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    class Meta:
        db_table = 'produtos'

"""
class Venda(models.Model):
    TIPO_PAGAMENTO = (
        (u'AV',u'A Vista'),
        (u'CH',u'Cheque'),
        (u'CT',u'Cartao'),    
    )
    id_venda = models.AutoField(primary_key=True)
    data_compra = models.DateField()
    valor_total = models.DecimalField(max_digits=19,decimal_places=2)
    metragem = models.IntegerField()
    preco_unidade = models.DecimalField(max_digits=19,decimal_places=2)
    tipo_pagamento = models.CharField(max_length=2,choices=TIPO_PAGAMENTO)
    id_produto = models.ForeignKey('Produto')
    id_cliente = models.ForeignKey('Cliente')
    
    class Meta:
        db_table = 'vendas'

class RetiradaFornecedor(models.Model):
    id_retirada_fornecedor = models.AutoField(primary_key=True)
    data_retirada = models.DateField()
    metros_retirados = models.DecimalField(max_digits=19,decimal_places=2)
    id_venda = models.ForeignKey('Venda')
    id_fornceddor = models.ForeignKey('Fornecedor')
    
    class Meta:
        db_table = 'retiradas_fornecedores'
    
    
class CompraFornecedor(models.Model):
    id_compra_fornecedor = models.AutoField(primary_key=True)
    data_compra = models.DateField()
    metros_comprados = models.DecimalField(max_digits=19,decimal_places=2)
    valor_da_compra = models.DecimalField(max_digits=19,decimal_places=2)
    id_fornecedor = models.ForeignKey('Fornecedor')

    class Meta:
        db_table = 'compras_fornecedores'

class Cheque(models.Model):
    id_cheque = models.AutoField(primary_key=True)
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    num_cheque = models.CharField(max_length=20)
    data_recebimento = models.DateField()
    data_vencimento = models.DateField()
    dono = models.CharField(max_length=60)
    valor = models.DecimalField(max_digits=19,decimal_places=2)
    id_cliente = models.ForeignKey('Cliente')
    id_venda = models.ForeignKey('Venda')

    class Meta:
        db_table = 'cheques'
"""

