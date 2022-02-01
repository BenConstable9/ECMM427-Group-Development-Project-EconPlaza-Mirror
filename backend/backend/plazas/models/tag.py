from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):

    name = models.SlugField("Tag's Slug", max_length=32)

    limit = models.Q(app_label="plazas", model="plaza") | models.Q(
        app_label="plazas", model="post"
    )
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, limit_choices_to=limit
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["tag", "content_type", "object_id"], name="no_duplicate_tags"
            ),
        ]

    def __str__(self):
        return f"{self.tag.name}"
