from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
import os
from django.conf import settings
from .models import Game
from django.views.generic import ListView

def platform(request):
    games = Game.objects.all()
    return render(request, "gamePlatform/platform.html", {'games' : games})

def logout_user(request):
    logout(request)
    return redirect('mainHome:home')

def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    return render(request, f'gamePlatform/games/{game.slug}/index.html', {'game': game})
