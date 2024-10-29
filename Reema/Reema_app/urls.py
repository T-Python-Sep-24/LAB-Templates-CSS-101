from django.urls import path
from . import views


app_name = "Reema_app"

urlpatterns = [
path("", views.Home_page, name="Home_page"),
path("html/introduction/", views.Contact_us, name="Contact_us"),
path("css/introduction/", views.Personal, name="Personal"),
path("article/ai/", views.Article, name="Article"),
path("careers/cv/", views.Careers, name="Careers"),

]


