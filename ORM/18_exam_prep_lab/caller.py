import os
from decimal import Decimal

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Actor, Director, Movie
from django.db.models import Q, F, Count, Avg, Case, When, Value, DecimalField


# Create queries within functions


def get_directors(search_name=None, search_nationality=None) -> str:
    if search_name is None and search_nationality is None:
        return ''
    elif search_name is not None and search_nationality is not None:
        query = Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality)
    elif search_name is not None:
        query = Q(full_name__icontains=search_name)
    elif search_nationality is not None:
        query = Q(nationality__icontains=search_nationality)

    found_directors = Director.objects.filter(query).order_by("full_name")

    if not found_directors:
        return ""

    result = []

    for director in found_directors:
        result.append(f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}")

    return "\n".join(result)


def get_top_director() -> str:
    top_director = Director.objects.get_directors_by_movies_count().first()

    if not top_director:
        return ""

    return f"Top Director: {top_director.full_name}, movies: {top_director.num_of_movies}."


def get_top_actor() -> str:
    top_actor = Actor.objects.annotate(
        starring_count=Count("movie__starring_actor"),
        avg_rating=Avg("movie__rating")
    ).order_by(
        "-starring_count",
        "full_name"
    ).first()

    if not top_actor or not top_actor.starring_count:
        return ""

    top_actor_starring_movies = Movie.objects.filter(starring_actor__full_name=top_actor.full_name)
    top_starring_movies = ", ".join(movie.title for movie in top_actor_starring_movies)

    return f"Top Actor: {top_actor.full_name}, starring in movies: {top_starring_movies}, movies average rating: {top_actor.avg_rating:.1f}"


def get_actors_by_movies_count() -> str:
    top_actors = Actor.objects.annotate(
        num_movies=Count("actors")
    ).order_by(
        "-num_movies",
        "full_name"
    )[:3]

    if not top_actors or not top_actors[0].num_movies:
        return ''

    return "\n".join(f"{actor.full_name}, participated in {actor.num_movies} movies" for actor in top_actors)


def get_top_rated_awarded_movie():
    top_rated_movie = Movie.objects.filter(
        is_awarded=True
    ).order_by(
        "-rating",
        "title",
    ).first()

    if not top_rated_movie:
        return ""

    actors_in_top_movie = top_rated_movie.actors.order_by('full_name').values_list("full_name", flat=True)
    starring_actor_in_top_movie = top_rated_movie.starring_actor.full_name if top_rated_movie.starring_actor else "N/A"

    return (f"Top rated awarded movie: {top_rated_movie.title}, rating: {top_rated_movie.rating:.1f}. "
            f"Starring actor: {starring_actor_in_top_movie}. Cast: {', '.join(actors_in_top_movie)}.")


def increase_rating():
    update_movie_ratings = Movie.objects.filter(
        is_classic=True,
        rating__lt=10,
    ).update(
        rating=F('rating') + 0.1
        )

    if not update_movie_ratings:
        return "No ratings increased."
    return f"Rating increased for {update_movie_ratings} movies."
