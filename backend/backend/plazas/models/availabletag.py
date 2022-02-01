from django.db import models
from django.utils.translation import gettext_lazy as _

class AvailableTag(models.Model):

    name = models.SlugField("Tag's Slug", max_length=32)

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"], name="no_duplicate_tag"
            ),
        ]

    def __str__(self):
        return f"{self.name}"
