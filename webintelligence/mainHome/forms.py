from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import *

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=100,
        required=True,
        label='ФИO',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Введите ваше ФИО'
        })
    )
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Придумайте логин'
        })
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Придумайте пароль'
        })
    )
    password2 = forms.CharField(
        label='Повтор пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Повторите пароль'
        })
    )
    role = forms.ChoiceField(
        label='Выберите роль',
        choices=Profile.ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-input'})
    )

    class Meta:
        model = User
        fields = ["username", "full_name", "password1", "password2", "role"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Сохраняем роль в профиле
            user.profile.role = self.cleaned_data['role']
            user.save()
        return user

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
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # Проверяем, введен email или логин
            try:
                validate_email(username)
                is_email = True
            except ValidationError:
                is_email = False
            
            # Ищем пользователя по email или username
            if is_email:
                user_model = get_user_model()
                try:
                    username = user_model.objects.get(email=username).username
                except user_model.DoesNotExist:
                    username = None
            
            self.user_cache = authenticate(
                request=self.request,
                username=username,
                password=password
            )
            
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data