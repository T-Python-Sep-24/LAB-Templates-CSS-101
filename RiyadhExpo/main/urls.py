from django.urls import path
from . import views

urlpatterns = [
    path('introduction/', views.introduction_view, name='introduction'),   
    path('about/', views.about_view, name='about'),   
    path('article/ai/', views.article, name='article'),
    path('book/',views.bookevent_view, name="book_event"),
]
