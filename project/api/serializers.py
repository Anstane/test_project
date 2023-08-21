from rest_framework import serializers

from models.models import (
    Musician,
    Album,
    Song
)


class MusicianSerializer(serializers.ModelSerializer):
    """Сериализатор модели музыканта."""

    class Meta:
        model = Musician
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор модели альбома."""

    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    """Сериализатор модели песни."""

    class Meta:
        model = Song
        fields = '__all__'
