# Generated by Django 3.2.11 on 2022-01-31 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Cloths',
        ),
    ]