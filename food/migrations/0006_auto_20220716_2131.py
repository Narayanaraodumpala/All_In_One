# Generated by Django 3.2.11 on 2022-07-16 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_rename_addfoodmodel_foodmodel'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='foodmodel',
            table='Food',
        ),
        migrations.AlterModelTable(
            name='restaurentmodel',
            table='Restaurents',
        ),
    ]
