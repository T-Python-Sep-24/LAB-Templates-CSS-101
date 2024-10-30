from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def main_view(request:HttpRequest):

    return render(request, "main/home.html")


def html_intro_view(request:HttpRequest):

    return render(request, "main/html_intro.html")


def css_intro_view(request:HttpRequest):

    return render(request, "main/css_intro.html")


def article_view(request:HttpRequest):

    return render(request, "main/my_ai_article.html")


def cv_view(request:HttpRequest):

    return render(request, "main/my_cv.html")
