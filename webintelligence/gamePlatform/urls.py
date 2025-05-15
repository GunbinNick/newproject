from django.urls import path
from .views import *

app_name = 'gamePlatform'

urlpatterns = [
    path('', platform, name="platform"),
    path('game/<slug:slug>', game_detail, name="game_detail"),
    path('logout/', logout_user, name='logout'),
]