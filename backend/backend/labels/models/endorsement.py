from django.db import models
from django.utils.translation import gettext_lazy as _

from . import Label


class Endorsement(models.Model):

    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
        verbose_name="Endorsement's label",
    )

    endorser = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        verbose_name="Endorsement's endorser",
    )

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    last_computed = models.DateTimeField("Last modified timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.report}"
