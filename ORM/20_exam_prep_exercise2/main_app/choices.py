from django.db import models


class TypesCategories(models.TextChoices):
    TECHNOLOGY = "Technology", "Technology"
    SCIENCE = "Science", "Science"
    EDUCATION = "Education", "Education"