# Generated by Django 5.0.1 on 2024-05-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_hub', '0006_alter_birthday_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='birthday',
            name='unique_birthday',
        ),
        migrations.AddConstraint(
            model_name='birthday',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'nickname', 'picture', 'user_id'), name='unique_birthday', violation_error_message='This person already exists.'),
        ),
    ]
