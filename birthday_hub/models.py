from django.contrib.auth.models import AbstractGroup
from django.contrib.auth.models import AbstractUser
from django.db import models


# Get the default profile picture
def default_profile_picture():
    return "birthday_hub/images/default_profile_picture.jpg"


class Birthday(models.Model):
    birthdate = models.DateField(blank=False, null=False)
    first_name = models.CharField(blank=False, null=False, max_length=50)
    last_name = models.CharField(blank=True, max_length=75)
    nickname = models.CharField(blank=True, max_length=50)
    notes = models.TextField(blank=True, help_text="Enter notes about this person and their birthday." ,max_length=250)
    picture = models.ImageField(blank=True, default=default_profile_picture ,upload_to="images/")

    # The user responsible for storing this birthday in the dabatase
    user_id = models.ForeignKey("User", blank=False, null=False, on_delete=models.CASCADE, related_name="birthdays", verbose_name="birthday's registrant")


    class Meta:
        # Define uniqueness constraint: a user can't register or store the same birthday more than once,
        # and the same person can't have two birthdates
        unique_together = [["first_name", "last_name", "nickname", "picture", "user_id"]]


    def __str__(self):
        return f"{self.first_name} {self.last_name} was born on {self.birthdate}."


# TODO
class Group(AbstractGroup):
    # Necessary so that after migrations are made, the group model can still be altered
    pass


class User(AbstractUser):
    birthdate = models.DateField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)


    def get_username(self):
        return self.username


    # Allow user not to inform first_name, in which case it will be set to the username
    first_name = models.CharField(blank=True, default=get_username ,null=False, max_length=50)
    last_name = models.CharField(blank=True, max_length=75)
    nickname = models.CharField(blank=True, max_length=50)
    picture = models.ImageField(blank=True, default=default_profile_picture ,upload_to="images/")


    def __str__(self):
        return f"{self.username} ({self.email}) was born on {self.birthdate}."
