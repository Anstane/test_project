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
    )
    list_filter = (
        'musician',
        'year',
    )
    search_fields = (
        'name',
        'musician',
        'year',
    )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_albums',
    )
    search_fields = (
        'name',
        'album',
    )

    def get_albums(self, obj):
        return '\n'.join([a.name for a in obj.album.all()])
