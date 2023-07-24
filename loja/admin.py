from django.contrib import admin
from .models import Produto

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_autor', 'marca','preco','descricao','imagem')