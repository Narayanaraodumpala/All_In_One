from rest_framework import serializers

from music.models import Album,Hero


class AlbumSerializers(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
          "__all__"
        )


class HeroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = (
          "__all__"
        )
