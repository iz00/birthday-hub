# Generated by Django 5.0.1 on 2024-03-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_hub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
