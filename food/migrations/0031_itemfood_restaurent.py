# Generated by Django 3.2.11 on 2022-10-14 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0030_auto_20221014_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemfood',
            name='restaurent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.restaurentmodel'),
        ),
    ]
