from django.urls import path
from django.shortcuts import render


def home(request):
    return render(request,'recipes/pages/index.html')


urlpatterns = [
    path('', home),

]
