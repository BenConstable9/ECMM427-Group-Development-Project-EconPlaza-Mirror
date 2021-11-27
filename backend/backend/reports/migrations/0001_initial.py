# Generated by Django 3.2.8 on 2021-11-27 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=64, verbose_name="Report's Model")),
                ('model_id', models.PositiveIntegerField(verbose_name='Model Key')),
                ('message', models.TextField(verbose_name="Report's Message")),
                ('state', models.CharField(choices=[('OP', 'Open'), ('CL', 'Closed')], default='OP', max_length=2, verbose_name="Report's State")),
                ('type', models.CharField(choices=[('OP', 'Open'), ('CL', 'Closed')], default='SP', max_length=2, verbose_name="Report's Type")),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at timestamp')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verdict', models.BooleanField(default=0, verbose_name="Review's Verdict")),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at timestamp')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports.report')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
