# Generated by Django 4.1.7 on 2023-04-01 22:15

import authentication.infrastructure.models
import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', authentication.infrastructure.models.BaseUserManager()),
                ('all_objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]