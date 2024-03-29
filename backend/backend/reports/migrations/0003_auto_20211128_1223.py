# Generated by Django 3.2.8 on 2021-11-28 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("reports", "0002_auto_20211128_1218"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="reporter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Report's User",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="report",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="reports.report",
                verbose_name="Response's Report",
            ),
        ),
        migrations.AlterField(
            model_name="response",
            name="reviewer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Response's User",
            ),
        ),
    ]
