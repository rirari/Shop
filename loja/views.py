from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm

# Create your views here.

def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produto_listar')
        else:
            print(form.errors)
    else:
        form = ProdutoForm()

    return render(request, 'loja/form.html', {'form': form})

def produto_listar(request):
    produtos = Produto.objects.all()
    context ={
        'produtos': produtos
    }
    return render(request, 'loja/index.html',context)

def detalhe_produto(request,id):
    produto = Produto.objects.get(id=id)
    context = {
        'produto':produto
    }
    return render(request,'loja/detalhe.html',context)

def produto_edicao(request):
    produtos = Produto.objects.all()
    context ={
        'produtos':produtos
    }
    return render(request, 'loja/produto.html',context)

def produto_editar(request,id):
    produto = get_object_or_404(Produto,id=id)
   
    if request.method == 'POST':
        form = ProdutoForm(request.POST,instance=produto)

        if form.is_valid():
            form.save()
            return redirect('produto_edicao')
    else:
        form = ProdutoForm(instance=produto)

    return render(request,"loja/form.html",{'form':form})

def produto_remover(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('produto_edicao') 

# def produto_criar(request):
#     if request.method == 'POST':
#         form = ProdutoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = ProdutoForm()
#     else:
#         form = ProdutoForm()

#     return render(request, "loja/form.html", {'form': form})

#def index(request):
   # total_produtos = Produto.objects.count()
   # context = {
     #   'total_produtos' : total_produtos,
    #}
    #return render(request, "loja/index.html",context)

# def index(request):
#     lista_index=Produto.objects.all()
#     context = {'objetos':lista_index}
#     return render(request,'loja/index.html',context)

