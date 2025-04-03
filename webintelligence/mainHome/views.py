from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from .forms import * 
from django.contrib.auth.models import User


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

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'mainHome/Register.html' 
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object

        #Парсинг ФИО 
        full_name = form.cleaned_data['full_name']
        parts = full_name.split()
        user.first_name = parts[0] if parts else ''
        user.last_name = ' '.join(parts[1:]) if len(parts) > 1 else ''
        user.save()
        
        login(self.request, user)
        return response
    
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'mainHome/Auth.html'
    #success_url = reverse_lazy('home')  
    
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)  # Сессия закроется при закрытии браузера
        response = super().form_valid(form)
        return response