# Generated by Django 3.2.11 on 2022-04-13 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_auto_20220413_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='hero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor', to='music.albumhero'),
        ),
    ]
