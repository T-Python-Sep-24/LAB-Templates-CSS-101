from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# Create your views here.
def html_view(request:HttpRequest):
    return render(request,"mini_projects/html_page.html")
