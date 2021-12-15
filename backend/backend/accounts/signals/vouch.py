from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.conf import settings

from ..models import Vouch, User

@receiver(post_save, sender=Vouch)
def verify_user(sender, instance, created, **kwargs):
    """Function to automatically verify the user if the vouches reaches the required level."""

    if created:
        # Get details of who has been vouched for
        received_vouchee = instance.vouchee

        total_vouchers_for_vouchee = Vouch.objects.filter(vouchee=received_vouchee.id).count()

        # See if we should now be verified
        if total_vouchers_for_vouchee >= settings.ECONPLAZA["QUANTITY_VOUCHES_FOR_VERIFICATION"]:
            # Verify the user
            vouchee_user = User.objects.get(id=received_vouchee.id)
            vouchee_user.verified = 1
            vouchee_user.save()

@receiver(post_delete, sender=Vouch)
def unverify_user(sender, instance, **kwargs):
    """Function to automatically unverify the user if the vouches drops below the required level."""

    # Get details of who has been vouched for
    received_vouchee = instance.vouchee

    total_vouchers_for_vouchee = Vouch.objects.filter(vouchee=received_vouchee.id).count()

    # See if we should now be unverified
    if total_vouchers_for_vouchee < settings.ECONPLAZA["QUANTITY_VOUCHES_FOR_VERIFICATION"]:
        # Unverify the user
        vouchee_user = User.objects.get(id=received_vouchee.id)
        vouchee_user.verified = 0
        vouchee_user.save()

