from django.urls import path
from . import views

app_name = "Lab"

urlpatterns = [
    path("", views.home_view, name= "home_view"),
    path("html/introduction/", views.thingsIlove_view, name="thingsIlove_view"),
    path("css/introduction/", views.thingsIlove_styled_view, name="thingsIlove_styled_view"),
    path("article/ai/", views.ai_veiw, name="ai_veiw"),
]
