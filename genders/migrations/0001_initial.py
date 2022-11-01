# Generated by Django 4.1.2 on 2022-11-01 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gender",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "genders",
                    models.CharField(
                        choices=[
                            ("Action", "Action"),
                            ("Animation", "Animation"),
                            ("Comedy", "Comedy"),
                            ("Horror", "Horror"),
                            ("NONE", "Default"),
                        ],
                        default="NONE",
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]
