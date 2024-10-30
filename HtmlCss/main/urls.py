from django.urls import path
from . import views
app_name = "main"
urlpatterns = [
    path("html/introduction/",views.html_intro,name="html_intro"),
    path("css/introduction/",views.css_intro,name="css_intro"),
    path("article/ai/",views.Ai,name="Ai"),
    path("careers/cv/",views.CV,name="cv")

]