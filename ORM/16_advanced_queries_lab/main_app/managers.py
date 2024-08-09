from django.db import models
from django.db.models import QuerySet


class ProductManager(models.Manager):
    def available_products(self) -> QuerySet:
        available_products = self.filter(is_available=True)
        return available_products

    def available_products_in_category(self, category_name: str) -> QuerySet:
        available_products_from_category = self.filter(is_available=True, category__name=category_name)
        return available_products_from_category

