from django.contrib import admin
from django.urls import path
from online_shop.mvc.views.views import index  # Adjusted import statement

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
