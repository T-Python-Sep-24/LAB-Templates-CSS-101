# mywebsite/main/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def ai_articles(request):
    return render(request, 'main/ai_articles.html')

def contact(request):
    return render(request, 'main/contact.html')

def hobbies(request):
    return render(request, 'main/hobbies.html')

def ai_revolution(request):
    return render(request, 'main/ai_revolution.html')  # Ensure this template exists