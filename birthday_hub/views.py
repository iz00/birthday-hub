from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import AddBirthdayForm, LoginForm, RegisterForm


@login_required(redirect_field_name=None)
def index(request):
    if request.method == "GET":
        form = AddBirthdayForm()
        context = {"form": form}
        return render(request, "birthday_hub/index.html", context)


@login_required(redirect_field_name=None)
def add_birthday(request):
    form = AddBirthdayForm(request.POST, request.FILES)
    form.instance.user_id = request.user

    try:
        form.save()
    except ValueError:
        context = {"form": form}
        return render(request, "birthday_hub/index.html", context)

    return redirect("birthday_hub:index")


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        context = {"form": form}
        return render(request, "birthday_hub/login.html", context)

    form = LoginForm(request, request.POST)

    if not form.is_valid():
        context = {"form": form}
        return render(request, "birthday_hub/login.html", context)

    username = form.cleaned_data["username"]
    password = form.cleaned_data["password"]

    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return redirect("birthday_hub:index")


def logout_view(request):
    logout(request)
    return redirect("birthday_hub:login")


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        context = {"form": form}
        return render(request, "birthday_hub/register.html", context)

    form = RegisterForm(request.POST)

    try:
        user = form.save()
    except ValueError:
        context = {"form": form}
        return render(request, "birthday_hub/register.html", context)

    login(request, user)
    return redirect("birthday_hub:index")
