from django.urls import path
from . import views

app_name='training'

urlpatterns=[
    path("",views.home_view,name='home_view'),
    path("html/introduction/",views.html_view,name='html_view'),
    path("css/introduction/",views.css_view,name='css_view'),
    path("article/ai/",views.article_view,name='article_view'),
    path("careers/cv/",views.cv_view,name='cv_ciew'),
]
