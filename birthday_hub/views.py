from django.shortcuts import render


def index(request):
    return render(request, "birthday_hub/index.html")
 