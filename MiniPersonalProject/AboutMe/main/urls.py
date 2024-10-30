from django.urls import path
from . import views

app_name ="main"

urlpatterns = [

    path('html/Hobbies/', views.Hobbies_view , name='Hobbies_view'),
    path('introduction/', views.introduction_view, name='introduction_view'), 
    path('article/ai/', views.article_view ,name='article_view'),
    path('careers/cv/', views.cv_view ,name='cv_view'),
]

