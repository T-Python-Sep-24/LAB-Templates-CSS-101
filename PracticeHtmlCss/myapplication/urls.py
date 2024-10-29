from django.urls import path
from . import views
app_name = "myapplication"
urlpatterns = [
    path("introduction",views.html_intro_view,name="html_intro_view"),
    path("introduction_css",views.css_intro_view,name="css_intro_view"),
    path("",views.article,name="article"),
    path("cv",views.cv,name="cv"),
]