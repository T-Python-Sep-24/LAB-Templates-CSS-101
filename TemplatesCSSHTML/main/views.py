from django.shortcuts import render
from django.http import HttpResponse , HttpRequest

# Create your views here.
def home(request : HttpRequest):
    return render(request , 'main/Introduction.html')
def style(request:HttpRequest):
    return render(request,'main/static/CSS/Introduction.css')