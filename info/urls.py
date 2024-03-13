from django.urls import path
from .views import ContentCRUD,TeacherView

urlpatterns = [
    path('post/',ContentCRUD.as_view()),
    path('get/',TeacherView.as_view())
]
