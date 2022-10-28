from django.contrib import admin
from .models import Album,AlbumHero,Audios , AddFavSongs,Hero

# Register your models here.
admin.site.register(Album)
admin.site.register(AlbumHero)
admin.site.register(Audios)
admin.site.register(AddFavSongs)
admin.site.register(Hero)