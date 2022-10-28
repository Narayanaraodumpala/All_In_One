# Generated by Django 3.2.11 on 2022-07-17 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0008_auto_20220716_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurentmodel',
            name='rest_username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]