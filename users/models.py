from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from feed_back.models import  FeedBack
from borroweds.models import Borrowed
import uuid

from borroweds.models import Borrowed


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    avatar = models.TextField(
        null=True,
        blank=True,
        default=None,
    )
    email = models.EmailField()
    birth = models.DateField()
    stars = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        default=5,
        editable=False,
    )

    REQUIRED_FIELDS = [
        "email",
        "birth",
    ]

    def get_nota(self)-> str:
        feeds = FeedBack.objects.all()
        valores = []
        for e in FeedBack.objects.all():
            valores.append(e)
       
        notas=[]
        for item in valores:
            nota = Borrowed.objects.get(feed_back = item)
            print(item,"1")
        print(valores)
        return "to"