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
        fields = ('name', 'id',)


class SongRepSerializer(serializers.ModelSerializer):
    """
    Вспомогательный сериализатор для отображения модели песни.
    """

    class Meta:
        model = Song
        fields = ('name', 'id',)


class AlbumRepSerializer(serializers.ModelSerializer):
    """
    Вспомогательный сериализатор для отображения модели альбома.
    """

    class Meta:
        model = Album
        fields = ('name', 'id',)


class SongSerializer(serializers.ModelSerializer):
    """Сериализатор модели песни."""

    musician = MusicianSerializer(many=True)
    album = AlbumRepSerializer(many=True)

    class Meta:
        model = Song
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    """Сериализатор модели альбома."""

    musician = MusicianSerializer()
    song = SongRepSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'
