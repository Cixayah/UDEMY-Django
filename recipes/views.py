from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(
        request,
        "recipes/index.html",
        context={
            "title": "Home",
            "content": "Welcome to the home page!",
        },
    )


def contact(request):
    return render(
        request,
        "recipes/contact.html",
        context={
            "title": "Contact",
            "content": "Contact us!",
        },
    )


def about(request):
    return HttpResponse("Hello, about!")
