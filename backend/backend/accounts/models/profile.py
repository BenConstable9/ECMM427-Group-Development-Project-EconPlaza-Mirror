from django.db import models
from django.utils.translation import gettext_lazy as _

from . import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        models.CASCADE,
        verbose_name="Profile's related user",
    )

    display_name = models.CharField("Profile's Display Name", max_length=30)

    global_anonymous = models.BooleanField(
        "Profile's Annoymous Flag", default=0)

    # Assumes reputation can never be negative
    reputation = models.PositiveBigIntegerField(
        "Profile's reputation (Computed)", default=0
    )

    created_at = models.DateTimeField(
        "Created at timestamp", auto_now_add=True)

    last_computed = models.DateTimeField(
        "Last modified timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
