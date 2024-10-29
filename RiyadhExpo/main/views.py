from django.shortcuts import render

def introduction_view(request):
    return render(request, 'main/introduction.html')

def about_view(request):
    return render(request, 'main/about.html')

def article(request):
    return render(request, 'main/article.html')

def bookevent_view(request):
    return render(request,'main/book_event.html')

