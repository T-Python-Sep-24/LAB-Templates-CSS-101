from django.urls import path
from . import views

app_name = 'html_css_app'

urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("html/introduction/", views.html_view, name='html_view'),
    path("css/introduction/", views.css_view, name='css_view'),
    path("article/ai/", views.ai_article_view, name='ai_article_view'),
    path("careers/cv", views.cv_view, name='cv_view'),
]
