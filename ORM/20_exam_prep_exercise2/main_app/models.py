from django.db import models

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from main_app.choices import TypesCategories
from main_app.managers import AuthorManager


# Create your models here.


class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3),
        ]
    )

    email = models.EmailField(
        unique=True,
    )

    is_banned = models.BooleanField(
        default=False,
    )

    birth_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2005),
        ],
    )

    website = models.URLField(
        blank=True,
        null=True,
    )

    objects = AuthorManager()


class Article(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5),
        ]
    )

    content = models.TextField(
        validators=[
            MinLengthValidator(10),
        ],
    )

    category = models.CharField(
        max_length=10,
        default=TypesCategories.TECHNOLOGY,
        choices=TypesCategories.choices,
    )

    authors = models.ManyToManyField(
        to=Author,
    )

    published_on = models.DateTimeField(
        editable=False,
        auto_now_add=True,
    )


class Review(models.Model):
    content = models.TextField(
        validators=[
            MinLengthValidator(10),
        ],
    )

    rating = models.FloatField(
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0),
        ],
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
    )

    article = models.ForeignKey(
        to=Article,
        on_delete=models.CASCADE,
    )

    published_on = models.DateTimeField(
        editable=False,
        auto_now_add=True,
    )