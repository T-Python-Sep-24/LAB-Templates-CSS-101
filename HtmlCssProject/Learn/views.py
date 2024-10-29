from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def welcome(request: HttpRequest):
    return HttpResponse("WELCOME")

def html_intro(request: HttpRequest):
    return render(request, "Learn/introToHtml.html")

def css_intro(request: HttpRequest):
    return render(request, "Learn/introToCss.html")

def ai_article(request: HttpRequest):
    return render(request, "Learn/aiArticle.html")

def my_cv(request: HttpRequest):
    return render(request, "Learn/myCV.html")

