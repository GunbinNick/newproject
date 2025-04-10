from django.urls import path
from .views import *

app_name = 'gamePlatform'

urlpatterns = [
    path('', platform, name="platform"),
    path('alphGame/', alphgameapp, name="alphGame"),
    path('numGame/', numsgameapp, name="numGame"),
    path('logout/', logout_user, name='logout'),
]