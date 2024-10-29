from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index_view(request:HttpRequest):
    return render(request,"myapplication/index.html")

def html_intro_view(request:HttpRequest):
    return render(request,"myapplication/introduction.html")

def css_intro_view(request:HttpRequest):
    return render(request, 'myapplication/introduction_css.html')

def article(request:HttpRequest):
    return render(request, "myapplication/article.html")

def cv(request:HttpRequest):
    return render(request, "myapplication/cv.html")





