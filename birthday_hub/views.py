from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginForm, RegisterForm


def index(request):
    return render(request, "birthday_hub/index.html")


def login(request):
    if request.method == "GET":
        form = LoginForm()
        context = {"form": form}
        return render(request, "birthday_hub/login.html", context)


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
    else:
        login(request, user)
        return HttpResponseRedirect(reverse("birthday_hub:index"))
