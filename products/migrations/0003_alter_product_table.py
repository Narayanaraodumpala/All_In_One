# Generated by Django 3.2.11 on 2022-01-27 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_product_category'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='Products',
        ),
    ]