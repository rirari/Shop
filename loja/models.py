from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    marca = models.CharField(max_length=150, verbose_name='Editora')
    preco = models.FloatField(verbose_name='Preço')
    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(upload_to='media/imagens')

    def __str__(self):
        return self.nome

    

