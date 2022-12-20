# Generated by Django 4.1.4 on 2022-12-20 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Integration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("request_id", models.UUIDField()),
                ("club_id", models.UUIDField()),
                ("method", models.CharField(max_length=100)),
                ("url", models.URLField()),
                ("login", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
            ],
        ),
    ]