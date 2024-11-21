from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def html_intro_view(request: HttpRequest):
    
    return render(request, "main/html-intro.html")

def css_intro_view(request: HttpRequest):

    return render(request, "main/css-intro.html")

def article_ai_view(request: HttpRequest):

    return render(request, "main/article-ai.html")

def career_cv_view(request: HttpRequest):

    return render(request, "main/career-cv.html")
    
def home_view(request: HttpRequest):

    return render(request, "main/home.html")