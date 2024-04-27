from django.contrib import admin
from django.urls import path
from online_shop.mvc.views.views import *  # Adjusted import statement

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
]
