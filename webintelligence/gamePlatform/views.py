from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
import os
from django.conf import settings
from .models import Game

def platform(request):
    return render(request, "gamePlatform/platform.html")

def logout_user(request):
    logout(request)
    return redirect('mainHome:home')

def game_list(request):
    """Список всех игр (без пагинации для простоты)."""
    games = Game.objects.all()  # Просто все игры
    print(games)
    return render(request, "games/game_list.html", {"games": games})

def game_detail(request, slug):
    """Отображение конкретной игры."""
    game = get_object_or_404(Game, slug=slug)
    return render(request, f"games/{game.slug}/index.html")  # Путь к игре
