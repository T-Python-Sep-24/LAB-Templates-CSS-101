from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.


def Hobbies_view(request:HttpRequest):
    return render(request, "main/Hobbies.html")

def introduction_view(request:HttpRequest):
    return render(request, "main/introduction.html")

def article_view(request:HttpRequest):
    return render(request, "main/Articles.html")


def cv_view(request:HttpRequest):
    return render(request, "main/cv.html")

