from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('html/introduction/', views.home, name='home'),
    path('css/introduction/', views.style, name='csspage'),
    path('careers/cv/', views.CV, name='CV'),
    path('article/ai/', views.AIrevolution, name='AI'),
]
