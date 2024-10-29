from django.shortcuts import render
from django.http import HttpRequest, HttpResponse



def html_intro_view(request:HttpRequest):
    return render(request,"introduction.html")

def css_intro_view(request:HttpRequest):
    return render(request, 'introduction_css.html')

def article(request:HttpRequest):
    return render(request, "article.html")

def cv(request:HttpRequest):
    return render(request, "cv.html")






