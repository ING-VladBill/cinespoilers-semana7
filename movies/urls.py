from django.urls import path
from .views import (
    MovieListView,
    GenreListView,
    ReviewListView
)


urlpatterns = [
    path(
        "movies/",
        MovieListView.as_view(),
        name="movie-list"
    ),

    path(
        "genres/",
        GenreListView.as_view(),
        name="genre-list"
    ),

    # NUEVO
    path(
        "reviews/",
        ReviewListView.as_view(),
        name="review-list"
    ),
]