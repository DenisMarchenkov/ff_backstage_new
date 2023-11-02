from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'search_field',
        'placeholder': 'Введите свой логин',
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'search_field',
        'placeholder': 'Введите свой пароль',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']
