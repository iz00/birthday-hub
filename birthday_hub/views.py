from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import AddBirthdayForm, LoginForm, RegisterForm
from .models import Birthday

@login_required(redirect_field_name=None)
def index(request):
    if request.method == "GET":
        form = AddBirthdayForm()
        context = {"form": form}
        return render(request, "birthday_hub/index.html", context)


@login_required(redirect_field_name=None)
def add_birthday(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=405)

    updated_request = request.POST.copy()
    updated_request.update({"user": request.user})

    form = AddBirthdayForm(updated_request, request.FILES)

    try:
        form.save()
    except ValueError:
        return JsonResponse({"errors": form.errors.as_json()}, status=400)

    return JsonResponse({"message": "Birthday added successfully."}, status=201)


@login_required(redirect_field_name=None)
def list_birthdays(request):
    if request.method != "GET":
        return JsonResponse({"error": "GET request required."}, status=405)

    birthdays = request.user.birthdays.order_by("first_name").all()
    return JsonResponse([birthday.serialize() for birthday in birthdays], safe=False, status=200)


@login_required(redirect_field_name=None)
def delete_birthday(request, birthday_id):
    if request.method != "DELETE":
        return JsonResponse({"error": "DELETE request required."}, status=405)

    try:
        Birthday.objects.get(pk=birthday_id, user=request.user).delete()
    except Birthday.DoesNotExist:
        return JsonResponse({"error": "Birthday not found."}, status=404)

    return JsonResponse({"message": "Birthday deleted successfully."}, status=200)


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
