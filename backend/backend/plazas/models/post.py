from django.db import models
from django.utils.translation import gettext_lazy as _

from . import Plaza


class Post(models.Model):
    profile = models.ForeignKey(
        "accounts.Profile",
        on_delete=models.CASCADE,
        verbose_name="Post's User Profile",
    )

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        verbose_name="Post's User",
    )

    plaza = models.ForeignKey(
        Plaza,
        on_delete=models.CASCADE,
        verbose_name="Post's Plaza",
    )

    title = models.CharField("Post's Title", max_length=128)

    content = models.TextField("Post's Content", blank=True)

    permissions = models.TextField(
        "Post's Permissions which is a serialised object", blank=True
    )

    reactions = models.TextField(
        "Post's Reactions which is a serialised object (Computed)", blank=True
    )

    hidden = models.BooleanField("Post's Hidden Flag", default=0)

    deleted = models.BooleanField("Post's Deleted Flag", default=0)

    views = models.PositiveIntegerField(
        "Post's Total Views (Computed)", default=0)

    created_at = models.DateTimeField(
        "Created at timestamp", auto_now_add=True)

    last_computed = models.DateTimeField(
        "Last modified timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.report}"
