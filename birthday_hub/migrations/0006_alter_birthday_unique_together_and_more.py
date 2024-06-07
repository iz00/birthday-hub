# Generated by Django 5.0.1 on 2024-05-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_hub', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='birthday',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='birthday',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'nickname', 'picture', 'user_id'), name='unique_birthday'),
        ),
    ]