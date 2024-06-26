# Generated by Django 5.0.3 on 2024-03-30 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0003_member_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(max_length=15)),
                ("address", models.TextField()),
                ("education", models.CharField(max_length=100)),
                ("profession", models.CharField(max_length=100)),
            ],
        ),
    ]
