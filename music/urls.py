from unicodedata import name
from django.contrib import admin
from django.urls import path, include

from products import views
from user import urls
from All_In_One import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from .views import UploadAlbum, audio ,add_fav,search_album,Hero,hero_albums,show_fav_songs,remove_favt_song

urlpatterns = [

    path('upload_album/', UploadAlbum.as_view(), name='upload_album'),
    path('audio/<str:pk>', audio, name='audio'),
    path('add_fav/<int:pk>',add_fav,name='add_fav'),
    path('search-album/',search_album,name='search-album'),
    path('actor/',Hero.as_view(),name='actor'),
    path('hero-albums/<str:pk>',hero_albums,name='hero-albums'),
    path('show_fav_songs/',show_fav_songs,name='show_fav_songs'),
    path('remove_favt_song/<str:pk>',remove_favt_song,name='remove_favt_song')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
