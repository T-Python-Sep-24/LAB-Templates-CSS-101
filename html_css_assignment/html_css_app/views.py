from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def main_view(request: HttpRequest):

    return render(request, 'main.html')


def html_view(request:HttpRequest):

    return render(request, 'htmlPage.html')


def css_view(request: HttpRequest):

    return render(request, 'cssPage.html')


def ai_article_view(request: HttpRequest):

    return render(request, 'aiArticle.html')


def cv_view(request: HttpRequest):

    return render(request, 'cv.html')