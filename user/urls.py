from django.urls import path
from .views import *

urlpatterns = [
    path('student/register/',RegisterStudent.as_view()),
    path('student/login/',LoginStudent.as_view()),
    path('teacher/register/',RegisterTeacher.as_view()),
    path('teacher/login/',LoginTeacher.as_view()),
]
