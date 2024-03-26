from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from .models import CustomUserCreationForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('homepage')  # Replace 'home' with the URL where you want to redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'users/user_login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user immediately after successful signup
            login(request, user)
            return redirect('homepage')  # Redirect to the home page after successful signup and login
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/user_register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('user_login')  # Redirect to the login page after logout
