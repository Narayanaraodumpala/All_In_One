# Generated by Django 3.2.11 on 2022-07-16 16:15

from django.db import migrations, models
import food.models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_auto_20220716_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodmodel',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='foodmodel',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='foodmodel',
            name='image3',
        ),
        migrations.AddField(
            model_name='foodmodel',
            name='image',
            field=models.FileField(null=True, upload_to=food.models.foodcatFile),
        ),
    ]