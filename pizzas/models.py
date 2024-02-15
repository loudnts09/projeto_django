from django.db import models

# Create your models here.


class Bordas(models.Model):
    tipo_borda = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bordas'


class Massas(models.Model):
    tipo_massa = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'massas'


class Sabores(models.Model):
    tipo_sabor = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sabores'
        
class Pizza(models.Model):
    borda = models.ForeignKey('Borda', on_delete=models.DO_NOTHING)
    massa = models.ForeignKey('Massa', on_delete=models.DO_NOTHING)
    pedidos = models.ForeignKey('Pedidos', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pizza'
        
        
class PizzaSabores(models.Model):
    pizza = models.ForeignKey('Pizza', models.DO_NOTHING)
    sabores = models.ForeignKey('Sabores', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pizza_sabores'