from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request, "mainHome/Main.html")

def about(request):
    return render(request, "mainHome/About.html")

def programs(request):
    return render(request, "mainHome/Programs.html")

def authorization(request):
    return render(request, "mainHome/Auth.html")

def register(request):
    return render(request, "mainHome/Register.html")
