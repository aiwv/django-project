from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'login__input',
        'placeholder': 'Username / e-mail'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'login__input',
        'placeholder' : 'Password'
    }))
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'Введите имя пользователя'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'Введите пароль'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : 'form-control py-4',
        'placeholder' : 'Подтвердите пароль' 
    }))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
