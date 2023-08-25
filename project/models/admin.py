from django.contrib import admin

from .models import (
    Musician,
    Album,
    Song
)


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'musician',
        'year',
        'get_songs',
    )
    list_filter = (
        'musician',
        'year',
    )
    search_fields = (
        'name',
        'musician',
        'year',
        'song',
    )

    def get_songs(self, obj):
        return '\n'.join([s.name for s in obj.song.all()])


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_albums',
        'get_musicians',
    )
    search_fields = (
        'name',
        'album',
        'musician',
    )

    def get_albums(self, obj):
        return '\n'.join([a.name for a in obj.album.all()])

    def get_musicians(self, obj):
        return '\n'.join([m.name for m in obj.musician.all()])
