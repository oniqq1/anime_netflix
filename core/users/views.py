
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
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


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
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('http://127.0.0.1:8000/steins-gate/')
    return render(request, 'users/logout.html')

@login_required
def profile_view(request):
    print(request.user.username)
    print(request.user.profile.nickname)

    return render(request, 'users/profile.html', {
        "user": request.user,
        "profile": request.user.profile,
    })


@login_required
def change_nickname(request):
    if request.method == 'POST':
        new_nickname = request.POST.get('nickname')
        if new_nickname:
            request.user.profile.nickname = new_nickname
            request.user.profile.save()
            return redirect('profile')
    return render(request, 'users/change_nickname.html')


@login_required
def change_avatar(request):
    if request.method == 'POST' and request.FILES.get('avatar'):
        avatar = request.FILES['avatar']
        request.user.profile.avatar = avatar
        request.user.profile.save()
        return redirect('profile')
    return render(request, 'users/change_avatar.html')

@login_required
def profile_settings(request):
    return render(request, "users/settings.html")
