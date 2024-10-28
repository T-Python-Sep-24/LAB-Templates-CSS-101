import os
from django.shortcuts import render
from django.http import HttpRequest

def home_view(request: HttpRequest):
    return render(request, "Lab/home.html")

def save_comments_to_file(comments):
    file_path = 'comments.txt' 
    with open(file_path, 'a') as file:
        for comment in comments:
            file.write(f"{comment['username']},{comment['email']},{comment['comment']}\n")

def load_comments_from_file():
    comments = []
    file_path = 'comments.txt'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                username, email, comment = line.strip().split(',')
                comments.append({'username': username, 'email': email, 'comment': comment})
    return comments

def get_context(request: HttpRequest):
    comments = load_comments_from_file()

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        if username and email and comment:
            comments.append({'username': username, 'email': email, 'comment': comment})
            save_comments_to_file(comments)

    favorite_shows = [
        {"title": "Dark", "rating": 8.7, "best_episode": "The Paradise", "seasons": 3},
        {"title": "The Last Kingdom", "rating": 8.5, "best_episode": "Season 3 Episode 8", "seasons": 6},
        {"title": "Vikings", "rating": 8.5, "best_episode": "All His Angels", "seasons": 6},
        {"title": "The Office", "rating": 9.0, "best_episode": "Dinner Party", "seasons": 9},
        {"title": "Brooklyn Nine-Nine", "rating": 8.4, "best_episode": "The Chopper", "seasons": 8},
    ]
    
    return {
        'comments': comments,
        'favorite_shows': favorite_shows
    }

def thingsIlove_view(request: HttpRequest):
    context = get_context(request)
    return render(request, "Lab/pageOne.html", context)

def thingsIlove_styled_view(request: HttpRequest):
    context = get_context(request)
    return render(request, "Lab/pageTwo.html", context)
