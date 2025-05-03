from django.urls import path
from .views import *

app_name = 'mainHome'

urlpatterns = [
    path('', Home, name="home"),
    path('about/', about, name="about"),
    path('programs/', programs, name="programs"),
    path('Contacts/', contacts, name="contacts"),
    path('News/', news, name="news"),
    path('Events/', events, name="events"),
    path('Franchise/', franchise, name="franchise"),
    path('Blog/', blog, name="blog"),
    path('authorization/', CustomLoginView.as_view(), name="auth"),
    path('register/', RegisterView.as_view(), name="register"),
]