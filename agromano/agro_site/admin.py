# nome_da_aplicacao/admin.py
from django.contrib import admin
from .models import Produto, ProdutoAll

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'disponivel', 'id',)  # Campos a serem exibidos na listagem
    list_filter = ('disponivel',)  # Filtros na barra lateral
    search_fields = ('nome', 'descricao')  # Campos de busca

@admin.register(ProdutoAll)
class ProdutoAllAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'disponivel', 'id',)  # Campos a serem exibidos na listagem
    list_filter = ('disponivel',)  # Filtros na barra lateral
    search_fields = ('nome', 'descricao')  # Campos de busca