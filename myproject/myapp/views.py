from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(request: HttpRequest):
    return render(request, 'myapp/home.html')

def about(request: HttpRequest):
    return render(request, 'myapp/about.html')

def contact(request: HttpRequest):
    return render(request, 'myapp/contact.html')

def cv(request: HttpRequest):
    return render(request, 'myapp/cv.html')

def ai(request):
    return render(request, 'myapp/ai.html')