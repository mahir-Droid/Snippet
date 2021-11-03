from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello, good evening!')

def eggs(request):
    return HttpResponse('Hello, good noon!')