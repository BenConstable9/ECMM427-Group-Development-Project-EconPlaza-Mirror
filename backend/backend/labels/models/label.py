from django.db import models
from django.utils.translation import gettext_lazy as _

class Label(models.Model):

    title = models.CharField("Label's Title", max_length=64)

    LABEL_TYPE_CHOICES = [
        ('SL', 'Skill'),
        ('GP', 'Group'), 
    ]

    label_type = models.CharField("Label's Type", max_length=2, choices=LABEL_TYPE_CHOICES, default='SL')

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.report}"
