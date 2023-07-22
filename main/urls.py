"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from loja.views import index, produto_criar, produto_editar, produto_listar, produto_remover, detalhe_produto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('produto/',produto_criar,name='produto_criar'),
    path('produto/editar/<int:id>/',produto_editar, name='produto_editar'),
    path('produto/remover/<int:id>/',produto_remover,name='produto_remover'),
    path('produto/listar',produto_listar,name='produto_listar'),
    path('detalhe/<int:id>/',detalhe_produto,name='detalhe_produto'),

]
