# Generated by Django 3.2.11 on 2022-01-27 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userdata_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
