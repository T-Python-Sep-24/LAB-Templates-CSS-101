from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("html/introduction/", views.html_intro_view, name = "html_intro_view"),
    path("css/introduction/", views.css_intro_view, name = "css_intro_view"),
    path("article/ai/", views.article_ai_view, name = "article_ai_view"),
    path("career/cv/", views.career_cv_view, name = "career_cv_view"),
]
