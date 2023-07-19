from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    marca = models.CharField(max_length=150)
    preco = models.FloatField()
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens',null=True,blank=True)

    def __str__(self):
        return self.nome

    

