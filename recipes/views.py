from django.http import HttpResponse

def home (request):
    return HttpResponse('Hello, home!')
def contact (request):
    return HttpResponse('Hello, contact!')

def about (request):
    return HttpResponse('Hello, about!')

