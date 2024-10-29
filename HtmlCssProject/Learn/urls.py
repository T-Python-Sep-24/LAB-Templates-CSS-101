from django.urls import path
from . import views

app_name = 'Learn'

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("html/introduction/", views.html_intro, name="html_intro"),
    path("css/introduction/", views.css_intro, name="css_intro"),
    path("article/ai/", views.ai_article, name="ai_article"),
    path("careers/cv/", views.my_cv, name="my_cv")
]