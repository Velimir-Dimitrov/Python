from django.db import models

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, RegexValidator
import datetime

from main_app.choices import Breaths
from main_app.managers import HouseManager


# Create your models here.


class Base(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=80,
        validators=[
            MinLengthValidator(5)
        ],
        unique=True,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
    )


class House(Base):
    motto = models.TextField(
        blank=True,
        null=True,
    )

    is_ruling = models.BooleanField(
        default=False,
    )

    castle = models.CharField(
        max_length=80,
        blank=True,
        null=True,
    )

    wins = models.PositiveSmallIntegerField(
        default=0
    )

    objects = HouseManager()


class Dragon(Base):
    power = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=1.0,
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(10.0)
        ]
    )

    breath = models.CharField(
        choices=Breaths.choices,
        default=Breaths.UNKNOWN,
        max_length=9,
    )

    is_healthy = models.BooleanField(
        default=True,
    )

    birth_date = models.DateField(
        default=datetime.date.today()
    )

    wins = models.PositiveSmallIntegerField(
        default=0,
    )

    house = models.ForeignKey(
        to=House,
        on_delete=models.CASCADE,
    )


class Quest(Base):
    name = models.CharField(
        max_length=80,
        validators=[
            MinLengthValidator(5)
        ],
        unique=True,
    )

    code = models.CharField(
        max_length=4,
        unique=True,
        validators=[
            MinLengthValidator(4),
            RegexValidator(regex=r"^[A-Za-z#]{4}$")
        ]
    )

    reward = models.FloatField(
        default=100.0
    )

    start_time = models.DateTimeField()

    modified_at = models.DateTimeField(
        auto_now=True
    )

    dragons = models.ManyToManyField(
        to=Dragon
    )

    host = models.ForeignKey(
        to=House,
        on_delete=models.CASCADE
    )
