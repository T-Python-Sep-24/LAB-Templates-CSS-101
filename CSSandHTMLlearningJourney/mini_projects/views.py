from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# Create your views here.
def html_view(request:HttpRequest):
    return render(request,"mini_projects/html_page.html")

def css_view(request):
    return render(request,"mini_projects/css_page.html")

def ai_view(request):
    return render(request, "mini_projects/ai.html")

def cv_view(request):
    return render(request, "mini_projects/cv.html")

def cv_work_view(request):
    return render(request, "mini_projects/cv_work.html")