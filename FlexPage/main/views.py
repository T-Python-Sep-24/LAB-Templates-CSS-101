from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest , HttpResponse 


def home_view(request:HttpRequest):
    
    return render(request , "main/home.html")

def introduction_view(request:HttpRequest):

    return render(request , "main/introduction.html")

def css_view(request:HttpRequest):

    return render(request , "main/csstest.html")

def article_ai_view(request:HttpRequest):
   
    return render(request,'main/articleAi.html')

def cv_view(request:HttpRequest):

    return render(request,'main/cvpage.html')