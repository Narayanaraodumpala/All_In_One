# Generated by Django 3.2.11 on 2022-06-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_alter_foodcategory_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFoodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField(default=False)),
                ('rname', models.CharField(max_length=30)),
                ('dname', models.CharField(max_length=40)),
                ('dtype', models.CharField(max_length=19)),
                ('dcat', models.CharField(max_length=20, null=True)),
                ('dprice', models.IntegerField()),
                ('image1', models.FileField(upload_to='')),
                ('image2', models.FileField(upload_to='')),
                ('image3', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_id', models.IntegerField()),
                ('rest_name', models.CharField(max_length=30)),
                ('rest_image', models.FileField(upload_to='')),
                ('rest_type', models.CharField(max_length=36, null=True)),
                ('rest_status', models.CharField(max_length=10)),
                ('rest_city', models.CharField(max_length=20, null=True)),
                ('rest_state', models.CharField(max_length=20, null=True)),
                ('rest_ratings', models.CharField(default=2.5, max_length=3, null=True)),
                ('rest_pincode', models.IntegerField(default=False)),
                ('rest_address', models.CharField(default=False, max_length=50)),
            ],
        ),
    ]
