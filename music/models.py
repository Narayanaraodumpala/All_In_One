from django.db import models
from django.contrib.auth.models import User


# Create your models here.
def albumFile(instance, filename):
    return '/'.join(['albums', str(instance.id), filename])

def herofile(instance, filename):
    return '/'.join(['hero', str(instance.id), filename])

def fav_songs(instance, filename):
    return '/'.join(['fav_song', str(instance.id), filename])


class AlbumHero(models.Model):
    hero = models.CharField(max_length=30)
    

    class Meta:
        db_table = 'hero'

    def __str__(self):
        return self.hero


class Album(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    album = models.CharField(max_length=100)
    album_hero = models.ForeignKey(AlbumHero, on_delete=models.CASCADE, related_name='album_hero', null=True)
    album_image = models.ImageField(upload_to=albumFile,
                                    max_length=254, blank=True, null=True)

    class Meta:
        db_table = 'album'

    def __str__(self):
        return self.album


class Audios(models.Model):
    song_name = models.CharField(max_length=100)
    song = models.FileField(upload_to='songs')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_song')
    duration=models.CharField(max_length=10)

    class Meta:
        db_table='Audios'

    def __str__(self):
        return self.song_name
    
# class AddFavSongs(models.Model):
#       track_name=models.CharField(max_length=100)
#       track=models.FileField(upload_to='fav_songs')
#       duration=models.CharField(max_length=30)
#       album=models.ImageField(upload_to=fav_songs,
#                                     max_length=254)
#       hero=models.CharField(max_length=50,null=True)
      
      
#       def __str__(self) :
#           return self.track



    
class AddFavSongs(models.Model):
      user=models.ForeignKey(User , on_delete=models.CASCADE)
      track_name=models.CharField(max_length=100)
      track=models.FileField(upload_to='fav_songs')
      duration=models.CharField(max_length=30)
      album=models.ImageField(upload_to=fav_songs,
                                    max_length=254)
      hero=models.CharField(max_length=50,null=True)
      
      
      def __str__(self) :
          return self.track_name
      
class Hero(models.Model):
    hero=models.ForeignKey(AlbumHero, on_delete=models.CASCADE, related_name='album_actor', null=True)
    image=models.ImageField(upload_to=herofile,
                                    max_length=254, blank=True, null=True)
    
    

    
    class Meta:
        db_table='actor'


