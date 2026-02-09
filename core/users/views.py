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
            return redirect('main-page')
    else:
        form = RegisterModel()
    return render(request, 'users/register.html', {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('main-page')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {"form": form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main-page')
    return render(request, 'users/logout.html')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {
        "user": request.user,
        "profile": request.user.profile
    })
