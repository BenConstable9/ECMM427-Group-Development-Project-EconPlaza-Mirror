from django.db import models
from django.utils.translation import gettext_lazy as _

from . import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="Comment's Post",
    )

    profile = models.ForeignKey(
        "accounts.Profile",
        on_delete=models.CASCADE,
        verbose_name="Comment's User Profile",
    )

    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        verbose_name="Comment's User",
    )

    content = models.TextField("Comment's Content", blank=True)

    reactions = models.TextField(
        "Comment's Reactions which is a serialised object (Computed)", blank=True
    )

    hidden = models.BooleanField("Comment's Hidden Flag", default=0)

    deleted = models.BooleanField("Comment's Deleted Flag", default=0)

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    last_computed = models.DateTimeField("Last modified timestamp")

    def __str__(self):
        return f"{self.report}"
