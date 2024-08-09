from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator

from main_app.choices import TypeOfStatus
from main_app.managers import AstronautManager


# Create your models here.


class Base(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2)
        ],
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )


class Astronaut(Base):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(regex=r'^[0-9]+$')
        ],
    )

    is_active = models.BooleanField(
        default=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    spacewalks = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ],
    )

    objects = AstronautManager()


class Spacecraft(Base):
    manufacturer = models.CharField(
        max_length=100,
    )

    capacity = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1)
        ],
    )

    weight = models.FloatField(
        validators=[
            MinValueValidator(0.0)
        ],
    )

    launch_date = models.DateField()


class Mission(Base):
    description = models.TextField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=9,
        choices=TypeOfStatus.choices,
        default="Planned",
    )

    launch_date = models.DateField()

    spacecraft = models.ForeignKey(
        to=Spacecraft,
        on_delete=models.CASCADE,
        related_name='spacecrafts'
    )

    astronauts = models.ManyToManyField(
        to=Astronaut,
    )

    commander = models.ForeignKey(
        to=Astronaut,
        null=True,
        on_delete=models.SET_NULL,
        related_name="commanders"
    )