# from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse('HOME')

def contact(request):
    return HttpResponse('CONTATO')

def about(request):
    return HttpResponse('SOBRE')

urlpatterns = [
    path('', home),
    path('contato/', contact),
    path('sobre/', about),
]
