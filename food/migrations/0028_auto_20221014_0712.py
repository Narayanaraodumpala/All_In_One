# Generated by Django 3.2.11 on 2022-10-14 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0027_alter_foodcart_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcart',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='foodcart',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
    ]