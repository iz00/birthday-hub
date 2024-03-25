from django.shortcuts import render

from .forms import RegisterForm


def index(request):
    return render(request, "birthday_hub/index.html")


def register(request):
    if request.method == "GET":
        form = RegisterForm()
        context = {"form": form}
        return render(request, "birthday_hub/register.html", context)
