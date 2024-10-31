from django.http import HttpRequest
from django.shortcuts import render

def view_html(request:HttpRequest):
    return render(request, "main/introduction.html")

def view_css(request:HttpRequest):
    return render(request, "main/css.html")

def view_article(request:HttpRequest):
    return render(request, "main/article.html")
def view_cv(request:HttpRequest):
    return render(request,"main/cv.html")

