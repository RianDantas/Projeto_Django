from django.db import models
from django.utils import timezone

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao =models.TextField()


    def __str__(self):
        self.nome