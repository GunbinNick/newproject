from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name="home"),
    path('about/', about, name="about"),
    path('programs/', programs, name="programs"),
    path('authorization/', CustomLoginView.as_view(), name="auth"),
    path('register/', RegisterView.as_view(), name="register"),
]