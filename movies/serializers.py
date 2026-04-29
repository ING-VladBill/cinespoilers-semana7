from rest_framework import serializers
from .models import Movie, Genre, Review


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = [
            "id",
            "name"
        ]


# NUEVO
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            "id",
            "reviewer_name",
            "rating",
            "comment",
            "created_at"
        ]


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(
        many=True,
        read_only=True
    )

    # NUEVO
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "release_date",
            "genres",
            "reviews"  # CAMBIO
        ]