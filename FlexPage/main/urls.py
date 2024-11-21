from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('html/introduction/', views.introduction_view, name='introduction_view'),
    path('css/introduction/' , views.css_view , name='css_view'),
    path('article/ai', views.article_ai_view , name='article_ai_view' ),
    path('careers/cv/' , views.cv_view , name='cv_view')
]
