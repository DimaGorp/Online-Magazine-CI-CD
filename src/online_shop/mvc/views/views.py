# mvc/views/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html')
def about(request):
    return render(request, 'about/about.html')
def contact(request):
    return render(request, 'contact/contact.html')
def service(request):
    return render(request, 'service/service.html')