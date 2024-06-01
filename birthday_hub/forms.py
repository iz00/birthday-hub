from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils import timezone

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
         # user field is included only to garantee checking UniqueConstraint in model
        fields = ["user", "first_name", "last_name", "nickname", "picture", "birthdate", "notes"]
        widgets = {
            # It does not appear to user
            "user": forms.HiddenInput(),
            "first_name": forms.TextInput(attrs={"autocomplete": "off", "placeholder": "Name"}),
            "last_name": forms.TextInput(attrs={"autocomplete": "off", "placeholder": "Last name"}),
            "nickname": forms.TextInput(attrs={"autocomplete": "off", "placeholder": "Nickname"}),
            "birthdate": forms.DateInput(attrs={"type": "date", "max": timezone.now().date()}),
            "notes": forms.Textarea(attrs={"autocomplete":"off", "cols": 80, "placeholder": "Notes here.", "rows": 5}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].required = False
