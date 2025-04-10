from django.shortcuts import render, redirect
from django.contrib.auth import logout
import os
from django.conf import settings

def platform(request):
    return render(request, "gamePlatform/platform.html")

def alphgameapp(request):
    template_path = os.path.join(
        settings.BASE_DIR, 'gamePlatform', 'games', 'alphGame', 'alph.html'
    )
    return render(request, template_path, context={})

def numsgameapp(request):
    template_path = os.path.join(
        settings.BASE_DIR, 'gamePlatform', 'games', 'numGame', 'num.html'
    )
    return render(request, template_path, context={})

def logout_user(request):
    logout(request)
    return redirect('mainHome:home')
