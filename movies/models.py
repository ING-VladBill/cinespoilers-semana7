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


# NUEVO
class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews"  # IMPORTANTE
    )

    reviewer_name = models.CharField(
        max_length=100
    )

    rating = models.IntegerField()  # 1 a 5 (lo validaremos luego si queremos)

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.reviewer_name} - {self.movie.title}"