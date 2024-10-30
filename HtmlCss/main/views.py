from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.

def html_intro(request:HttpRequest):
    
    return render(request,"main/html_intro.html")

def css_intro(request:HttpRequest):
    return render(request,"main/css_intro.html")


def Ai(request:HttpRequest):
    return render(request,"main/Ai.html")

def CV(request:HttpRequest):
    return render(request,"main/cv.html")