from django.urls import path
from . import views
app_name = "myapplication"
urlpatterns = [
    path("",views.index_view,name="index_view"),
    path("introduction",views.html_intro_view,name="html_intro_view"),
    path("introduction_css",views.css_intro_view,name="css_intro_view"),
    path("article",views.article,name="article"),
    path("cv",views.cv,name="cv"),
]