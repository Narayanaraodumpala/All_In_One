# Generated by Django 3.2.11 on 2022-09-28 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0021_itemfoodmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemfoodmodel',
            name='food_item_category',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
