# Generated by Django 3.2.11 on 2022-10-14 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0031_itemfood_restaurent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemfood',
            name='restaurent',
        ),
    ]
