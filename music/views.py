import json
from django.http import HttpResponse
from django.shortcuts import redirect, render, redirect
from django.views import View
from rest_framework.generics import ListAPIView
from .serializers import AlbumSerializers, HeroSerializers
from django.core.paginator import Paginator

from music.models import Album, Audios, AddFavSongs, Hero
from django.contrib.auth.decorators import login_required


class UploadAlbum(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializers

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Album.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


def audio(request, pk):
    print('pk=', pk)
    album = Album.objects.filter(album=pk).first()
    print(album.album_hero)
    print(album.album)
    print(album.album_image.url)
    audios = Audios.objects.filter(album__album=pk)

    return render(request, 'music/audios.html', {'audios': Audios.objects.filter(album__album=pk),
                                                 'album': album.album, 'album_hero': album.album_hero,
                                                 'total_audios': audios.count(),
                                                 'alb_image': album.album_image.url},
                  )


@login_required(login_url='login_signup')
def add_fav(request, pk):
    print(' song pk=', pk)
    fav_song = Audios.objects.get(id=pk)
    track_name = fav_song.song_name
    track = fav_song.song
    album = fav_song.album.album
    hero = fav_song.album.album_hero
    duration = fav_song.duration
    user = request.user

    print('user=', user)
    song = AddFavSongs.objects.filter(user=user, track_name=track_name).first()
    if not song:
        data = AddFavSongs.objects.create(user=user, track_name=track_name, track=track, album=album, hero=hero,
                                          duration=duration)
        # return render( request, 'music/addfavsongs.html',{'res':AddFavSongs.objects.filter(user=request.user)})
        return redirect('show_fav_songs')
    else:
        album = Album.objects.filter(album=pk).first()
        return render(request, 'home/music.html', {'song_error': 'sorry this song is alredy in A.D.F list'}, )

    pass


def search_album(request):
    search = request.POST['Search']
    print('search=', search)

    if search:
        res = Album.objects.filter(album__icontains=search)

        print('res=', res)
        if res:
            return render(request, 'home/music.html', {'res': res})
        else:

            return render(request, 'home/music.html', {'mesg': 'sorry , no album is avilable withthis search'})
    else:

        return render(request, 'home/music.html', {'info': 'please enter what you want to browse'})


class Hero(ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializers

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Hero.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


def hero_albums(request, pk):
    print('pk=', pk)
    data = Album.objects.filter(album_hero=pk)
    print('data=', data)
    return render(request, 'home/music.html', {'data': data})


def show_fav_songs(request):
    return render(request, 'music/addfavsongs.html', {'res': AddFavSongs.objects.filter(user=request.user)})


def remove_favt_song(request, pk):
    song = AddFavSongs.objects.filter(user=request.user, track_name=pk).delete()
    return redirect('show_fav_songs')
