from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Musician(models.Model):
    """Класс модели музыканта."""

    name = models.CharField(
        max_length=150, unique=True
    )

    def __str__(self):
        return self.name


class Album(models.Model):
    """Класс модели альбома."""

    name = models.CharField(
        max_length=150, unique=True
    )
    musician = models.ForeignKey(
        Musician,
        related_name='album',
        on_delete=models.CASCADE
    )
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(2023)
        ]
    )

    def __str__(self):
        return self.name


class Song(models.Model):
    """Класс модели песни."""

    name = models.CharField(
        max_length=150, unique=True
    )
    album = models.ManyToManyField(
        Album,
        related_name='song'
    )

    def __str__(self):
        return self.name
