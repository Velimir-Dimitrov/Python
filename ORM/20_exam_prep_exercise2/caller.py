import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from django.db.models import Q, Count, Avg, Max
from main_app.models import Author, Review, Article

# Create queries within functions


def get_authors(search_name=None, search_email=None) -> str:
    if search_name is None and search_email is None:
        return ""
    query_name = Q(full_name__icontains=search_name)
    query_email = Q(email__icontains=search_email)

    if search_name is not None and search_email is not None:
        query = Q(query_name & query_email)
    elif search_name is not None:

        query = query_name
    else:
        query = query_email

    found_authors = Author.objects.filter(query).order_by('-full_name')

    return "\n".join(f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}" for a in found_authors) if found_authors else ""


def get_top_publisher() -> str:
    top_author = Author.objects.get_authors_by_article_count().filter(
        article_count__gt=0
    ).order_by(
        '-article_count', 'email'
    ).first()

    return f"Top Author: {top_author.full_name} with {top_author.article_count} published articles." if top_author else ""


def get_top_reviewer() -> str:
    top_reviewer = Author.objects.annotate(
        num_of_reviews=Count('review')
    ).filter(
        num_of_reviews__gt=0
    ).order_by(
        '-num_of_reviews', 'email'
    ).first()

    return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.num_of_reviews} published reviews." if top_reviewer else ""


def get_latest_article() -> str:
    last_published_article = Article.objects.prefetch_related('review_set__author', 'review_set').order_by('-published_on').first()

    if last_published_article is None:
        return ""

    authors_on_article = ', '.join(author.full_name for author in last_published_article.authors.all().order_by('full_name'))
    num_reviews = last_published_article.review_set.count()
    avg_rating = sum([r.rating for r in last_published_article.review_set.all()]) / num_reviews if num_reviews else 0.0

    return f"The latest article is: {last_published_article.title}. Authors: {authors_on_article}. Reviewed: {num_reviews} times." \
           f" Average Rating: {avg_rating:.2f}."


def get_top_rated_article() -> str:
    top_rated_article = Article.objects.annotate(
        top_rating=Max('review__rating'),
        avg_rating=Avg('review__rating'),
        num_reviews=Count('review__rating')
    ).filter(
        top_rating__isnull=False
    ).order_by('-avg_rating', 'title').first()

    if not top_rated_article or top_rated_article.num_reviews == 0:
        return ""

    return (f"The top-rated article is: {top_rated_article.title}, "
            f"with an average rating of {top_rated_article.avg_rating:.2f}, "
            f"reviewed {top_rated_article.num_reviews} times.")


def ban_author(email=None) -> str:
    if email is None:
        return "No authors banned."

    banned_author = Author.objects.filter(email=email).first()

    if not banned_author or not Author.objects.all():
        return "No authors banned."

    banned_author.is_banned = True
    banned_author.save()

    deleted_reviews = Review.objects.filter(author__email=email).delete()[0]

    return f"Author: {banned_author.full_name} is banned! {deleted_reviews} reviews deleted."
