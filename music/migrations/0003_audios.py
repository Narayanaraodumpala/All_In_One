# Generated by Django 3.2.11 on 2022-01-31 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20220131_0552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('song', models.FileField(upload_to='')),
                ('duration', models.CharField(max_length=10)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_song', to='music.album')),
            ],
            options={
                'db_table': 'Audios',
            },
        ),
    ]