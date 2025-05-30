from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render


def home(request):
    return render(request,'recipes/index.html')

def contact(request):
    return HttpResponse('CONTATO')

def about(request):
    return HttpResponse('<h1>SOBRE recipes.views')

urlpatterns = [
    path('', home),
    path('contato/', contact),
    path('sobre/', about),
]
