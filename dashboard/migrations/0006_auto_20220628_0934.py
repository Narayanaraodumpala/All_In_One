# Generated by Django 3.2.11 on 2022-06-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_feedback_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='date',
        ),
        migrations.AddField(
            model_name='feedback',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
