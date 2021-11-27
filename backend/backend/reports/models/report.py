from django.db import models
from django.utils.translation import gettext_lazy as _

class Report(models.Model):
    reporter = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )

    model = models.CharField("Report's Model", max_length=64)

    # FIX: This model key might be incorrect

    model_id = models.PositiveIntegerField("Model Key")

    message = models.TextField("Report's Message")

    STATE_CHOICES = [
        ('OP', 'Open'),
        ('CL', 'Closed'), 
    ]

    state = models.CharField("Report's State", max_length=2, choices=STATE_CHOICES, default='OP')

    TYPE_CHOICES = [
        ('SP', 'Spam'),
        ('IP', 'Inappropriate'), 
        ('OT', 'Other'), 
    ]

    type = models.CharField("Report's Type", max_length=2, choices=STATE_CHOICES, default='SP')

    created_at = models.DateTimeField("Created at timestamp", auto_now_add=True)

    def __str__(self):
        return f"{self.report}"
