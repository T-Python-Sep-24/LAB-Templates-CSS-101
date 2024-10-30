from django.urls import path
from . import views


app_name='mini_projects'

urlpatterns=[
    path('html/introduction/',views.html_view,name="html_view"),
    path('css/introduction/',views.css_view,name='css_view'),
    path("article/ai/",views.ai_view,name="ai_view" ),
    path("careers/cv/",views.cv_view,name="cv_view"),
    path("careers/cv/work",views.cv_work_view,name="cv_work_view"),
]