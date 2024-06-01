from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


# Get the default profile picture from /media
def default_profile_picture():
    return "images/default_profile_picture.jpg"


class Birthday(models.Model):
    birthdate = models.DateField(blank=False, null=False)
    first_name = models.CharField(blank=False, null=False, max_length=50)
    last_name = models.CharField(blank=True, max_length=75, null=True)
    nickname = models.CharField(blank=True, max_length=50, null=True)
    notes = models.TextField(blank=True, help_text="Enter notes about this person and their birthday.", max_length=250, null=True)
    picture = models.ImageField(blank=True, default=default_profile_picture, null=False, upload_to="images/")

    # The user responsible for storing this birthday in the dabatase
    user = models.ForeignKey("User", blank=False, null=False, on_delete=models.CASCADE, related_name="birthdays", verbose_name="birthday's registrant")


    class Meta:
        # Define uniqueness constraint: a user can't register or store the same birthday more than once,
        # and the same person can't have two birthdates
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "last_name", "nickname", "user"],
                name='unique_birthday',
                # Since some of the fields can be null, and SQLite compares nulls as distinct in unique constraints
                # Force it to compare nulls as equals
                nulls_distinct=False,
                violation_error_message="This person already exists.")
        ]


    def clean(self):
        if self.birthdate and self.birthdate > timezone.now().date():
            raise ValidationError({"birthdate": "The birthdate must be in the past."})


    def __str__(self):
        return f"{self.first_name} {self.last_name} was born on {self.birthdate}."


# TODO
class Group(Group):
    # Necessary so that after migrations are made, the group model can still be altered
    pass


class User(AbstractUser):
    birthdate = models.DateField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)

    # Allow user not to inform first_name, in which case it will be set to the username
    first_name = models.CharField(blank=True, null=False, max_length=50)
    last_name = models.CharField(blank=True, max_length=75, null=True)
    picture = models.ImageField(blank=True, default=default_profile_picture, null=False, upload_to="images/")


    def __str__(self):
        return f"{self.username} ({self.email}) was born on {self.birthdate}."


    # Set first_name before saving the user's model
    def save(self, *args, **kwargs):
        if not self.first_name:
            if len(self.username) > 50:
                self.first_name = self.username[:50]
            else:
                self.first_name = self.username
        super().save(*args, **kwargs)
