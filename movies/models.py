from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    release_date = models.DateField()

    genres = models.ManyToManyField(
        Genre,
        related_name="movies"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title