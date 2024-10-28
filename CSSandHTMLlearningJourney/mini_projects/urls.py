from django.urls import path
from . import views


app_name='mini_projects'

urlpatterns=[
    path('html/introduction/',views.html_view,name="html_view"),
]