from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def home_view(request:HttpRequest):
    return render(request,'training/index.html')

def html_view(request:HttpRequest):

    return render(request,'training/htmlIntroduction.html')

def css_view(request:HttpRequest):

    return render(request,'training/css.html')

def article_view(request:HttpRequest):

    return render(request,'training/article_ai.html')

def cv_view(request:HttpRequest):

    return render(request,'training/CV.html')