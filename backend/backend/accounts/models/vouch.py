from django.db import models
from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError

from . import User


class Vouch(models.Model):

    voucher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="related_voucher_vouch",
        verbose_name="Vouch's voucher",
    )

    vouchee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="related_vouchee_vouch",
        verbose_name="Vouch's vouchee",
    )

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['voucher', 'vouchee'], name='no_duplicate_vouches'),
        ]

    def clean(self):
        if self.voucher == self.vouchee:
            raise ValidationError('Voucher and vouchee cannot be the same user.')

    def __str__(self):
        return f"{self.voucher}"
