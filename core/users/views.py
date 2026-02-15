from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterModel, LoginForm
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import random
import logging

logger = logging.getLogger(__name__)


def email_verification(user_email):
    subject = "Verification Email"
    num = random.randint(100000, 999999)
    message = f"Your verification code is: {num}"
    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", None)
    send_mail(subject, message, from_email, [user_email], fail_silently=False)
    logger.info("Email verification email sent", extra={'user_email': user_email})
    return num


def register_view(request):
    if request.method == 'POST':
        form = RegisterModel(request.POST)
        if form.is_valid():
            num = email_verification(form.cleaned_data['email'])
            request.session['verification_code'] = num
            request.session['registration_data'] = form.cleaned_data
            return redirect('email_verification')

    else:
        form = RegisterModel()
        logger.info("Registration page opened", extra={'username': request.user.username if request.user.is_authenticated else None})
    return render(request, 'users/register.html', {"form": form})


def email_verification_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        if code and int(code) == request.session.get('verification_code'):

            data = request.session.get('registration_data')

            if not data:
                logger.warning(f"No registration data found in session during email verification , user={request.user.username if request.user.is_authenticated else None}")
                return redirect('register')

            form = RegisterModel(data)

            if form.is_valid():
                user = form.save()

                login(request, user)
                logger.info(f"Email verification email sent , user={user.username}")

                request.session.pop('verification_code', None)
                request.session.pop('registration_data', None)

                return redirect("steins_gate_page")
    logger.info(f'Email verification page opened , user={request.user.username if request.user.is_authenticated else None}')
    return render(request, 'users/email_verification.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = redirect("steins_gate_page")
            response.set_cookie(key="username", value=user.username, max_age=60 * 60 * 24 * 3, httponly=True,
                                secure=False)
            logger.debug(f"User logged in , user={user.username}")
            return response
    else:
        form = LoginForm()
        logger.info(f"Login page opened , user={request.user.username if request.user.is_authenticated else None}")
    return render(request, 'users/login.html', {"form": form})


@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        logger.debug(f"User logged out , user={request.user.username}")
        return redirect("steins_gate_page")
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
            logger.debug(f"Nickname changed , user={request.user.username} new_nickname={new_nickname} ")
            return redirect('profile')


    return render(request, 'users/change_nickname.html')


@login_required
def change_avatar(request):
    if request.method == 'POST' and request.FILES.get('avatar'):
        avatar = request.FILES['avatar']
        request.user.profile.avatar = avatar
        request.user.profile.save()
        logger.debug(f"Avatar changed , user={request.user.username} , avatar={avatar.name} ")
        return redirect('profile')
    return render(request, 'users/change_avatar.html')


@login_required
def profile_settings(request):
    return render(request, "users/settings.html")
