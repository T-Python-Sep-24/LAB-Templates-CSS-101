from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def page_introduction(request:HttpRequest):
    return render(request,'app_HC/introduction.html')

def page_careers(request:HttpRequest):
    return render(request,'app_HC/careers.html')


def page_article(request:HttpRequest):
    return render(request,'app_HC/article.html')