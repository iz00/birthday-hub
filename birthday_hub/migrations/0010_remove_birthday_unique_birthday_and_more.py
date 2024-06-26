# Generated by Django 5.0.1 on 2024-05-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_hub', '0009_remove_birthday_unique_birthday_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='birthday',
            name='unique_birthday',
        ),
        migrations.AddConstraint(
            model_name='birthday',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'nickname', 'picture', 'user'), name='unique_birthday', nulls_distinct=False, violation_error_message='This person already exists.'),
        ),
    ]
