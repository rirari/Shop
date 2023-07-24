from django.db import models

# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome do livro')
    nome_autor = models.CharField(max_length=200, verbose_name='Nome do autor(a)')
    marca = models.CharField(max_length=150, verbose_name='Editora')
    preco = models.FloatField(verbose_name='Preço')
    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(upload_to = 'imagens')

    def __str__(self):
        return self.nome

