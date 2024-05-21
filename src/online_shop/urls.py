# /src/online_shop/urls.py

from django.contrib import admin
from django.urls import path, include
from online_shop.mvc.views.views import *  # Adjusted import statement

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('shop_single/', shop_single, name='shop_single'),
    path('shop_single_huli/', shop_single_huli, name='shop_single_huli'),
    path('shop_single_dragi/', shop_single_dragi, name='shop_single_dragi'),
    path('shop_single_fog/', shop_single_fog, name='shop_single_fog'),
    path('shop_single_mykola/', shop_single_mykola, name='shop_single_mykola'),
    path('shop_single_skuf/', shop_single_skuf, name='shop_single_skuf'),
    path('shop_single_arci/', shop_single_arci, name='shop_single_arci'),
    path('shop_single_dack/', shop_single_dack, name='shop_single_dack'),
    path('shop_single_pinin/', shop_single_pinin, name='shop_single_pinin'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('order/', order, name='order')
]
