from django.db.models.signals import post_save
from django.dispatch import receiver

from ..models import User, Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        display_name = instance.first_name + " " + instance.last_name

        Profile.objects.create(user=instance, display_name=display_name)
