# Generated by Django 3.2.11 on 2022-04-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0015_alter_hero_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='hero',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
