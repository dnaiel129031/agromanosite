# nome_da_aplicacao/models.py
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='agro_site/static/agro_site/images/', blank=True, null=True)  # Campo para imagem do produto, opcional
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nome
    
class ProdutoAll(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='agro_site/static/agro_site/images/', blank=True, null=True)  # Campo para imagem do produto, opcional
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nome