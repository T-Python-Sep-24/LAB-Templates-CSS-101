from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

#Mini CV Project Home page
def miniCVHomeView(request: HttpRequest):
    
    return render(request, "miniCVProject/cvHome.html")

#Display projects page
def projectsView(request: HttpRequest):
    
    return render(request, "miniCVProject/projects.html")

#Display skills page
def skillsView(request: HttpRequest):
    
    return render(request, "miniCVProject/skills.html")