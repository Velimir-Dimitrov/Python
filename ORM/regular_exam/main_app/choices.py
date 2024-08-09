from django.db import models


class TypeOfStatus(models.TextChoices):
    PLANNED = "Planned", "Planned"
    ONGOING = "Ongoing", "Ongoing"
    COMPLETED = "Completed", "Completed"