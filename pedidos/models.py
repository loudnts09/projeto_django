from django.db import models

# Create your models here.


class Pedidos(models.Model):
    status = models.ForeignKey('Status', on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pedidos'
        
        
class Status(models.Model):
    situação = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'status'