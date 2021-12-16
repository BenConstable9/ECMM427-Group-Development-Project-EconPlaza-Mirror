# Generated by Django 3.2.8 on 2021-12-16 17:45

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_vouch_voucher_and_vouchee_cannot_be_same'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='vouch',
            constraint=models.CheckConstraint(check=models.Q(('voucher', django.db.models.expressions.F('vouchee')), _negated=True), name='not_same'),
        ),
    ]
