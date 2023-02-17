from django.urls import path
from .views import UserListAPIView


app_name = 'TODOapp'
urlpatterns = [
    path('', UserListAPIView.as_view()),
]
