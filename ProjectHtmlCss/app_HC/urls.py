from django.urls import path
from . import views

app_name = 'app_HC'

urlpatterns = [
    path("", views.page_introduction, name="introduction"),
    path("careers/cv/", views.page_careers, name="careers"),
    path("article/cv/", views.page_article, name="article"),
    
    
]