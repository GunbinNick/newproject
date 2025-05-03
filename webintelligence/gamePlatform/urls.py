from django.urls import path
from .views import *

app_name = 'gamePlatform'

urlpatterns = [
    path('', platform, name="platform"),
    path("games/", game_list, name="game-list"),
    path("games/<slug:slug>/", game_detail, name="game-detail"),
    path('logout/', logout_user, name='logout'),
]