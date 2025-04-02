from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name="home"),
    path('about/', about, name="about"),
    path('programs/', programs, name="programs"),
    path('authorization/', authorization, name="auth"),
    path('register/', register, name="register"),
]