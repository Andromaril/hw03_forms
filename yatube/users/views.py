from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def users_out(request):
    """View - функция для страницы выхода из системы."""

    return render(request, 'users/logged_out.html')

@login_required
def password_change(request):
    """View - функция для страницы смены пароля."""

    return render(request, 'users/password_change_form.html')


def login(request):
    """View - функция для страницы входа в аккаунт."""

    return render(request, 'users/login.html')


def password_change_done(request):
    """View - функция для уведомления об удачной смене пароля."""

    return render(request, 'users/password_change_done.html')


def password_reset(request):
    """View - функция для изменения пароля через email."""

    return render(request, 'users/password_reset_form.html')


def password_reset_done(request):
    """View - функция для уведемления для отправки
       ссылки о смене пароля на email.
    """

    return render(request, 'users/password_reset_done.html')


def password_reset_confirm(request):
    """View - функция для страницы смены пароля,
       пользователь попадает сюда из письма.
    """

    return render(request, 'users/password_reset_confirm.html')


def password_reset_complete(request):
    """View - функция для уведомления о том, что пароль изменен."""

    return render(request, 'users/password_reset_complete.html')


class SignUp(CreateView):
    """Класс для отображения формы регистрации."""

    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'
