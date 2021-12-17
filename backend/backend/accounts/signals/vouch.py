from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.conf import settings

from ..models import Vouch, User

def should_be_verified(user_id):
    """Function to determine if we should verify a user."""

    # Count the total vouches
    total_vouchers_for_user = Vouch.objects.filter(vouchee=user_id).count()

    if total_vouchers_for_user >= settings.ECONPLAZA["QUANTITY_VOUCHES_FOR_VERIFICATION"]:
        return 1
    else:
        # Check if they are verified by a staff member as this overrides the limit for vouches
        staff = User.objects.filter(is_staff=True)
        total_vouchers_by_staff = Vouch.objects.filter(vouchee=user_id, voucher__in=staff.values('id')).count()

        if total_vouchers_by_staff >= 1:
            return 1
        else:
            return 0

@receiver(post_save, sender=User)
def verify_staff(sender, instance, created, **kwargs):
    """Function to automatically verify staff members."""

    modified_user = User.objects.get(id=instance.id)

    # If they have been set to staff then verify them
    if modified_user.is_staff:
        verified = 1
    else:
        # The user could have been unstaffed but still have enough verifications
        verified = should_be_verified(instance.id)

    # Use update to stop recursion by calling this signal again
    User.objects.filter(id=instance.id).update(verified=verified)

@receiver(post_save, sender=Vouch)
def verify_user(sender, instance, created, **kwargs):
    """Function to automatically verify the user if the vouches reaches the required level."""

    if created:
        # Get details of who has been vouched for
        received_vouchee = instance.vouchee

        vouchee_user = User.objects.get(id=received_vouchee.id)

        # Don't modify the verification for staff
        if not vouchee_user.is_staff:

            vouchee_user.verified = should_be_verified(received_vouchee.id)
            vouchee_user.save()

@receiver(post_delete, sender=Vouch)
def unverify_user(sender, instance, **kwargs):
    """Function to automatically unverify the user if the vouches drops below the required level."""

    # Get details of who has been vouched for
    received_vouchee = instance.vouchee

    vouchee_user = User.objects.get(id=received_vouchee.id)

    # Don't modify the verification for staff
    if not vouchee_user.is_staff:

        vouchee_user.verified = should_be_verified(received_vouchee.id)
        vouchee_user.save()