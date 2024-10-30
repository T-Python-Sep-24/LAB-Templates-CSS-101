from django.urls import path
from . import views

app_name = "Main"

urlpatterns = [
    path("html/introduction/", views.intro_view, name="intro_view"),
    path("css/introduction/", views.css_intro_view, name="css_intro_view"),
    path("article/ai/", views.articale_view, name="articale_view"),
    path("careers/cv/", views.cv_view, name="cv_view"),
    


]
