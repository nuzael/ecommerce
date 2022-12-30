from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('sobre/', about, name='about'),
    path('produtos/', products, name='products'),
    path('contato/', contact, name='contact'),
    path('busca/', search, name='search'),
    path('produtos/categoria/<int:pk>', category_products, name='category-products'),
    path('produtos/marca/<int:pk>', brand_products, name='brand-products'),
    path('produto/<str:slug>', single_product, name='single-product'),
    
    path('favoritos/', favorite, name='favorite'),
    path('adicionar-favorito/<str:slug>', ad_to_favorite, name='ad-to-favorite'),
    path('deletar-favorito/<str:slug>', del_to_favorite, name='del-to-favorite'),
    
    path('carrinho/', cart, name='cart'),
    path('adicionar-carrinho/<str:slug>', ad_to_cart, name='ad-to-cart'),
    path('deletar-carrinho/<str:slug>', del_to_cart, name='del-to-cart'),
    path('compra/', purchase, name='purchase'),
    
    path('perfil/', profile, name='profile'),
    path('entrar/', login, name='login'),
    path('registrar/', register, name='register'),
    path('sair/', logout, name='logout')
]