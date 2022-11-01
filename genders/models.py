from django.db import models
import uuid

class Gender(models.TextChoices):
    ACTION = "Action"
    ANIMATION = "Animation"
    COMEDY = "Comedy"
    HORROR = "Horror"
    DEFAULT = "NONE"

class Gender(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    genders = models.CharField(
        max_length=100,
        choices = Gender.choices,
        default = Gender.DEFAULT
    )