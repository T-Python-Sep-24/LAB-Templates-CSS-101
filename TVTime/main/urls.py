from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("html/introduction/", views.html_intro_view, name="html_intro"),
    path("css/introduction/", views.css_intro_view, name="css_intro"),
    path("article/ai/", views.article_view, name="my_ai_article"),
    path("careers/cv/", views.cv_view, name="my_cv"),

]