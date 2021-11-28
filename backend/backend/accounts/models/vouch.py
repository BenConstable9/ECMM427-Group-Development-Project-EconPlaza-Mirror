from django.db import models
from django.utils.translation import gettext_lazy as _

from . import User

class Vouch(models.Model):

    voucher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='related_voucher_vouch',
        verbose_name="Vouch's voucher",
    )

    vouchee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='related_vouchee_vouch',
        verbose_name="Vouch's vouchee",
    )

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.report}"
