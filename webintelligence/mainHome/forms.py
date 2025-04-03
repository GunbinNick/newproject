from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Введите ваше ФИО'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Придумайте логин'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Придумайте пароль'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Повторите пароль'
        })
    )

    class Meta:
        model = User
        fields = ["username", "full_name", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин или Email",
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Введите ваш логин или email',
            'id': 'login-input'
        })
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Введите ваш пароль',
            'id': 'password-input'
        })
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'remember-checkbox',
            'id': 'remember-me'
        })
    )