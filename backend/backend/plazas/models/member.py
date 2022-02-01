from django.db import models
from django.utils.translation import gettext_lazy as _

from . import Plaza


class Member(models.Model):

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        verbose_name="Plaza Membership's User",
    )

    plaza = models.ForeignKey(
        Plaza,
        on_delete=models.CASCADE,
        verbose_name="Plaza Membership's Plaza",
    )

    MEMBER_TYPE_CHOICES = [
        ("OP", "Owner"),
        ("AD", "Admin"),
        ("MB", "Member"),
    ]

    member_type = models.CharField(
        "Member Type", max_length=2, choices=MEMBER_TYPE_CHOICES, default="MB"
    )

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "plaza"], name="no_duplicate_memberships"
            ),
        ]

    def __str__(self):
        return f"{self.user}"
