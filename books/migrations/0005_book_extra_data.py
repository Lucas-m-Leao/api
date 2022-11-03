# Generated by Django 4.1.2 on 2022-11-03 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("extra_datas", "0001_initial"),
        ("books", "0004_book_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="extra_data",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="books",
                to="extra_datas.extra_data",
            ),
            preserve_default=False,
        ),
    ]
