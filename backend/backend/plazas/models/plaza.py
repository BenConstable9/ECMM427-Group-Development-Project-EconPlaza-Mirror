from django.db import models
from django.utils.translation import gettext_lazy as _


class Plaza(models.Model):

    slug = models.SlugField("Plaza's Slug", max_length=32)

    name = models.CharField("Plaza's Name", max_length=32)

    description = models.TextField("Plaza's Message", blank=True)

    permissions = models.TextField(
        "Plaza's Permissions which is a serialised object", blank=True
    )

    created_at = models.DateTimeField(
        "Created at timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
