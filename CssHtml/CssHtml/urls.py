from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('html/introduction/', views.view_html, name='view_home'),                 # For introduction.html
    path('css/introduction/', views.view_css, name='view_css'),
    path('article/ai/', views.view_article, name='view_article'),
    path('careers/cv/', views.view_cv,name="cv")
]
