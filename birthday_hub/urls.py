from django.urls import path

from . import views

app_name = "birthday_hub"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/birthday/", views.add_birthday, name="add_birthday"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
]
