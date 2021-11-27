from django.db import models
from django.utils.translation import gettext_lazy as _

from . import Report

class Response(models.Model):
    report = models.ForeignKey(
        'Report',
        on_delete=models.CASCADE,
    )

    reviewer = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )

    verdict = models.BooleanField("Review's Verdict", default=0)

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.report}"
