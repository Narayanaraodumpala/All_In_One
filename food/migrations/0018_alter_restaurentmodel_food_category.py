# Generated by Django 3.2.11 on 2022-09-22 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0017_alter_restaurentmodel_food_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurentmodel',
            name='food_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.foodcategory'),
        ),
    ]