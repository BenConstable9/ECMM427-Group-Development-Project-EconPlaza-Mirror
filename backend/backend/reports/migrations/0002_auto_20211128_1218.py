# Generated by Django 3.2.8 on 2021-11-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="report",
            name="type",
        ),
        migrations.AddField(
            model_name="report",
            name="report_type",
            field=models.CharField(
                choices=[("SP", "Spam"), ("IP", "Inappropriate"), ("OT", "Other")],
                default="SP",
                max_length=2,
                verbose_name="Report's Type",
            ),
        ),
        migrations.AlterField(
            model_name="report",
            name="message",
            field=models.TextField(blank=True, verbose_name="Report's Message"),
        ),
    ]
