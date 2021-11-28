from django.db import models
from django.utils.translation import gettext_lazy as _

from . import Label

class UserLabel(models.Model):

    label = models.ForeignKey(
        Label,
        on_delete=models.CASCADE,
        verbose_name="User's label",
    )

    # Assumes endorsements can never be negative
    endorsements = models.PositiveBigIntegerField("User's endorsements (Computed)", default=0)

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.report}"
