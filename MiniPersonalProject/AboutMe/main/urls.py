from django.urls import path
from . import views

app_name ="main"

urlpatterns = [

    path('/index/', views.introduction_view, name="introduction_view")

]