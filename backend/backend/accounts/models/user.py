from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    verified = models.BooleanField("User's Verified Flag", default=0)

    banned = models.BooleanField("User's Banned Flag", default=0)

    twitter_oauth = models.CharField("User's Twitter OAuth", max_length=16)

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    institutional_affiliation = models.CharField(
        "User's main institution", null=True, max_length=64
    )

    def __str__(self):
        return f"{self.username}"
