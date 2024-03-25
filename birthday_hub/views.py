from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import RegisterForm


def index(request):
    return render(request, "birthday_hub/index.html")


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        context = {"form": form}
        return render(request, "birthday_hub/register.html", context)

    if form.isvalid():
        user = form.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
