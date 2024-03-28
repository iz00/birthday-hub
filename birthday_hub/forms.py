from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Birthday, User


class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "first_name", "last_name", "birthdate", "picture", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"autocomplete": "off", "placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"autocomplete": "off", "placeholder": "email@example.com"}),
            "first_name": forms.TextInput(attrs={"autocomplete": "off", "placeholder": "Name"}),
            "last_name": forms.TextInput(attrs={"autocomplete": "off", "placeholder": "Last name"}),
            "birthdate": forms.DateInput(attrs={"type": "date"}),
        }


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"autocomplete": "off", "placeholder": "Username"}),
        }


class AddBirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = ["first_name", "last_name", "nickname", "picture", "birthdate", "notes"]
        widgets = {
            "first_name": forms.TextInput(attrs={"autocomplete": "off", "placeholder": "Name"}),
            "last_name": forms.TextInput(attrs={"autocomplete": "off", "placeholder": "Last name"}),
            "nickname": forms.TextInput(attrs={"autocomplete": "off", "placeholder": "Nickname"}),
            "birthdate": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"autocomplete":"off", "cols": 80, "placeholder": "Notes here.", "rows": 5}),
        }
