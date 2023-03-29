from django.shortcuts import render, HttpResponseRedirect
from .models import User
from django.urls import reverse
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:success'))
    else:
        form = UserLoginForm()


    context = {'form': form}
    return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

def success(request):
        return render(request, 'users/success.html')
