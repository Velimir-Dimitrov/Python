from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from main_app.managers import ProfileManager
# Create your models here.


class CreationDate(models.Model):
    class Meta:
        abstract = True

    creation_date = models.DateTimeField(
        auto_now_add=True,
    )


class Profile(CreationDate):
    full_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(limit_value=2)
        ],
    )

    email = models.EmailField()

    phone_number = models.CharField(
        max_length=15,
    )

    address = models.TextField()

    is_active = models.BooleanField(
        default=True,
    )

    objects = ProfileManager()


class Product(CreationDate):
    name = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(limit_value=0.01),
        ],
    )

    in_stock = models.PositiveIntegerField(
        validators=[
            MinValueValidator(limit_value=0),
        ],
    )

    is_available = models.BooleanField(
        default=True,
    )


class Order(CreationDate):
    profile = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )

    products = models.ManyToManyField(
        to=Product,
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(limit_value=0.01),
        ],
    )

    is_completed = models.BooleanField(
        default=False,
    )