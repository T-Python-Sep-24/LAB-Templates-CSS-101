from django.urls import path
from . import views

app_name = "HTMLAndCSS"

urlpatterns = [
    path("", views.htmlAndcssHome, name="htmlcssHomeView"),
    path("html/introduction/", views.htmlIntro, name="htmlIntroView"),
    path("css/introduction/", views.cssIntro, name="cssIntroView"),
    path("article/ai/", views.advancedHtmlCssView, name="advancedHtmlCssView")
]