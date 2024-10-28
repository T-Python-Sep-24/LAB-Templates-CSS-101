from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

#Mini CV Project Home page
def miniCVHomeView(request: HttpRequest):
    
    return render(request, "miniCVProject/cvHome.html")