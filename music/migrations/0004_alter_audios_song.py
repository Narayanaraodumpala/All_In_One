# Generated by Django 3.2.11 on 2022-01-31 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_audios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audios',
            name='song',
            field=models.FileField(upload_to='songs'),
        ),
    ]