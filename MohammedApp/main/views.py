from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):  # Updated function name
    return render(request, 'main/projects.html')  # Updated template name

def contact(request):
    if request.method == 'POST':
        # Handle the form submission here
        print(request.POST)
    return render(request, 'main/contact.html')

def cv(request):
    return render(request, 'main/cv.html')
