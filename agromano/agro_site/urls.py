# nome_da_aplicacao/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.products, name='products'),
    path('sobre/', views.about, name='about'),
    path('contato/', views.contact, name='contact'),
    path('send_whatsapp/<int:produto_id>/', views.send_whatsapp, name='send_whatsapp'),
]
