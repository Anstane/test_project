from django.urls import include, path
from rest_framework import routers

from .views import (
    MusicianViewSet,
    AlbumViewSet,
    SongViewSet
)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'musician', MusicianViewSet)
router.register(r'album', AlbumViewSet)
router.register(r'song', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
