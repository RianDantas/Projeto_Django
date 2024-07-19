from django.db import models
from django.utils import timezone

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.CharField(max_length=200,default=0)
    descricao =models.TextField()


    def __str__(self):
       return self.nome
    
    