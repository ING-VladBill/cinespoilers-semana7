from rest_framework import generics
from .models import Movie, Genre, Review
from .serializers import (
    MovieSerializer,
    GenreSerializer,
    ReviewSerializer
)


class MovieListView(generics.ListAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreListView(generics.ListAPIView):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# NUEVO
class ReviewListView(generics.ListAPIView):

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer