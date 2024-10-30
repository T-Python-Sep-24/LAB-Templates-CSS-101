from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import secrets
import string
# Create your views here.


def intro_view(request : HttpRequest):
    return render(request, "main/intro.html")

def css_intro_view(request : HttpRequest):
    return render(request, "main/css_intro.html")

def articale_view(request : HttpRequest):
    return render(request, "main/articale.html")

def cv_view(request : HttpRequest):
    return render(request, "main/index.html")
