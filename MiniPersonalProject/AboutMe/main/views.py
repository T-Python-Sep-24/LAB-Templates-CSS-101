from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.

def introduction_view(request:HttpRequest):
    return render(request, "main/src/index.html")




