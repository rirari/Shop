from django import forms
from .models import Produto
from django.forms import ModelForm

class ProdutoForm(ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'marca' : forms.TextInput(attrs={'class': 'form-control' }),
            'preco' : forms.NumberInput(attrs={'class': 'form-control' }),
            'descricao': forms.TextInput(attrs={'class': 'form-control' }),
            'imagem': forms.FileInput(attrs={'class': 'form-control' })
            
        }
