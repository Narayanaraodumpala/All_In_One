# Generated by Django 3.2.11 on 2022-06-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('dashboard_type', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Dashboard Types',
            },
        ),
    ]
