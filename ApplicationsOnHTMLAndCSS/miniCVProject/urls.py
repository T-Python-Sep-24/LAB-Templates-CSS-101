from django.urls import path
from . import views

app_name = "miniCVProject"

urlpatterns = [
    path("", views.miniCVHomeView, name="miniCVHomeView"),
    path("projects", views.projectsView, name="projectsView"),
    path("skills", views.skillsView, name="skillsView"),
]