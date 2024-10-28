from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

#Home page
def homeView(request: HttpRequest):
    
    return render(request, "mainApp/home.html")
