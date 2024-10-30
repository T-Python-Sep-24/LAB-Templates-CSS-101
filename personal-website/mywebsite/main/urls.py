# mywebsite/main/urls.py
from django.urls import path
from .views import home, about, projects, ai_articles, contact, hobbies, ai_revolution  # Ensure ai_revolution is imported

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('ai_articles/', ai_articles, name='ai_articles'),
    path('contact/', contact, name='contact'),
    path('hobbies/', hobbies, name='hobbies'),
    path('ai_revolution/', ai_revolution, name='ai_revolution'),  # Ensure this line exists
]