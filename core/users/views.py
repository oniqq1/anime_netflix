from django.shortcuts import render , redirect
from .forms import RegisterModel , LoginForm
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = RegisterModel(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)

            return redirect('main-page')
            #надо сделать редирект на главную страницу

        else:
            return render(request, 'users/register.html', {"form": form})
            #надо сделать редирект на страницу регистрации с сообщением об ошибке
            #то есть должно быть место для отображения ошибок в шаблоне регистрации



    form = RegisterModel()
    return render(request, 'users/register.html', {"form": form})

    #форма регистрации та же


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main-page')
    return render(request, 'users/logout.html')
    #страничка с кнопкой "Выйти" и формой для отправки POST запроса на logout_view

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main-page')

        # если честно , я не уверен на счет метода get_user() ,
        # но он должен возвращать объект пользователя ,
        # который существует


    form = LoginForm()
    return render(request, 'users/login.html', {"form": form})
    #ну там тоже форма для логина и кнопка для отправки POST запроса на login_view
    # и место для отображения ошибок в шаблоне логина

@login_required
def profile_view(request):
    #эта страница должна быть доступна только для авторизованных пользователей
    #на ней должно отображаться имя пользователя , email и аватарка
    #ну и там может быть кнопка для выхода из аккаунта , которая будет отправлять POST запрос на logout_view

    user = request.user
    return render(request, 'users/profile.html', {"user": user})







