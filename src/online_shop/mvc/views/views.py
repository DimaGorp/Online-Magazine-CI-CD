# mvc/views/views.py
from django.shortcuts import render
from ..models import Product
def index(request):
    return render(request, 'index/index.html')
def about(request):
    return render(request, 'about/about.html')
def contact(request):
    return render(request, 'contact/contact.html')
def service(request):
    return render(request, 'service/service.html')

def shop_single(request):
    return render(request, 'shop_single/shop_single.html')
def shop_single(request):
    return render(request, 'shop_single/shop_single.html')
def shop_single_arci(request):
    return render(request, 'shop_single/shop_single_arci.html')
def shop_single_dack(request):
    return render(request, 'shop_single/shop_single_dack.html')
def shop_single_dragi(request):
    return render(request, 'shop_single/shop_single_dragi.html')
def shop_single_fog(request):
    return render(request, 'shop_single/shop_single_fog.html')
def shop_single_huli(request):
    return render(request, 'shop_single/shop_single_huli.html')
def shop_single_mykola(request):
    return render(request, 'shop_single/shop_single_mykola.html')
def shop_single_pinin(request):
    return render(request, 'shop_single/shop_single_pinin.html')

def shop_single_skuf(request):
    return render(request, 'shop_single/shop_single_skuf.html')


def shop(request):
   # `products = Product.objects.all()` retrieves all instances of the `Product` model from the
   # database.
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'shop/shop.html',context)

def cart(request):
    return render(request, 'cart/cart.html')
