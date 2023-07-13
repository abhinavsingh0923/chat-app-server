from django.urls import path
from . import views

urlpatterns = [
    path('allstudents/',views.allstudents.as_view()),
]
