from rest_framework import viewsets

from models.models import (
    Musician,
    Album,
    Song
)
from .serializers import (
    MusicianSerializer,
    AlbumSerializer,
    SongSerializer
)


class MusicianViewSet(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
