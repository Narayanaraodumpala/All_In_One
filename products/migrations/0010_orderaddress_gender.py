# Generated by Django 3.2.11 on 2022-05-30 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20220527_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderaddress',
            name='gender',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
