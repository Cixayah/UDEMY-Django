from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from recipes.views import home, contact, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contact/', contact),
    path('about/', about),
]
