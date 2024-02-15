# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cliente'


class ClienteEndereco(models.Model):
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING)
    endereco = models.ForeignKey('Endereco', models.DO_NOTHING)

    class Meta:
        app_label = 'cadastro'
        managed = False
        db_table = 'cliente_endereco'


class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endereco'
