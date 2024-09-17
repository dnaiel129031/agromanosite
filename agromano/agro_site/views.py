from django.shortcuts import render
from .models import Produto, ProdutoAll
from datetime import datetime, time
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from urllib.parse import quote

def currentYear():
    current_year = datetime.now().year
    return current_year

def home(request):
    current_year = currentYear()
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'agro_site/home.html', {'produtos': produtos, 'current_year': current_year})

def products(request):
    current_year = currentYear()
    produtos_all = ProdutoAll.objects.filter(disponivel=True)
    search = request.GET.get('search', None)
    if search:
        produtos_all = produtos_all.filter(nome__icontains=search)
    # if not search:
    #     produtos_all = HttpResponse('Campo de busca vaziu')
    return render(request, 'agro_site/produtos.html', {'produtos_all': produtos_all,'current_year': current_year},)

def about(request):
    current_year = currentYear()
    return render(request, 'agro_site/sobre.html',{'current_year': current_year})

def contact(request):
    current_year = currentYear()
    return render(request, 'agro_site/contato.html',{'current_year': current_year})

def send_whatsapp(request, produto_id):
    # Busca o produto pelo ID
    produto = ProdutoAll.objects.get(id=produto_id)
    
    # Monta a mensagem
    texto = f"""
    *Nova Solicitação:*

    Olá, gostaria de comprar o produto abaixo:

    *{produto.nome}*
    *R${produto.preco:.2f}*

    *Link do Produto:*
    {request.build_absolute_uri(produto.imagem.url)}
    """

    # Codifica a mensagem para o formato correto do WhatsApp
    encoded_texto = quote(texto)

    # Monta a URL do WhatsApp com a mensagem codificada
    whatsapp_url = f"https://wa.me/554733265159?text={encoded_texto}"

    # Redireciona o usuário para o WhatsApp
    return HttpResponseRedirect(whatsapp_url)