# /src/online_shop/urls.py

from django.contrib import admin
from django.urls import path, include
from online_shop.mvc.views.views import *  # Adjusted import statement
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('shop_single/<int:product_id>/', shop_single, name='shop_single'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('order/', order, name='order')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)