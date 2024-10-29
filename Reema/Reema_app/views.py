from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.
def Home_page(request : HttpRequest):
 
  return render(request, "Reema_app\Home_page.html")


def Contact_us(request : HttpRequest):
 
  return render(request,"Reema_app\Contact_us.html" )


def Personal(request : HttpRequest):
 
  return render(request,"Reema_app\Personal.html" )


def Article(request : HttpRequest):
 
  return render(request,"Reema_app\Article.html" )


def Careers(request : HttpRequest):
 
  return render(request,"Reema_app\Careers.html" )







