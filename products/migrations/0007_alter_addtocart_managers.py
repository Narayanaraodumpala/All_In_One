# Generated by Django 3.2.11 on 2022-05-24 06:13

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_addtocart'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='addtocart',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
