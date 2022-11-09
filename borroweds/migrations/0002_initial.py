# Generated by Django 4.1.2 on 2022-11-09 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("borroweds", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrowed",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="borrowed",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
