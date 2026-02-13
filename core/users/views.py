
from http.client import responses

from django.shortcuts import render , redirect
from .forms import RegisterModel , LoginForm
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterModel, LoginForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterModel(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('http://127.0.0.1:8000/steins-gate/')
    else:
        form = RegisterModel()
    return render(request, 'users/register.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = redirect('http://127.0.0.1:8000/steins-gate/')
            response.set_cookie(key="username", value=user.username, max_age=60 * 60 * 24 * 3, httponly=True, secure=False)
            return response
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {"form": form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('http://127.0.0.1:8000/steins-gate/')
    return render(request, 'users/logout.html')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {
        "user": request.user,
        "profile": request.user.profile,
    })

@login_required
def profile_settings(request):
    return render(request, "users/settings.html")

