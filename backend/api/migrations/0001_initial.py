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
            name="Team",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, unique=True)),
                ("country", models.CharField(max_length=80)),
                ("principal", models.CharField(max_length=120)),
                ("car_name", models.CharField(max_length=120)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Driver",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("number", models.PositiveIntegerField()),
                ("nationality", models.CharField(max_length=80)),
                ("podiums", models.PositiveIntegerField(default=0)),
                ("world_titles", models.PositiveIntegerField(default=0)),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="drivers",
                        to="api.team",
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "number")},
            },
        ),
        migrations.CreateModel(
            name="Race",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("grand_prix_name", models.CharField(max_length=120)),
                ("location", models.CharField(max_length=120)),
                ("race_date", models.DateField()),
                ("circuit_name", models.CharField(max_length=120)),
                ("laps", models.PositiveIntegerField()),
                (
                    "winner_driver",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="wins",
                        to="api.driver",
                    ),
                ),
            ],
            options={
                "ordering": ["race_date"],
                "unique_together": {("grand_prix_name", "race_date")},
            },
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ticket_holder_name", models.CharField(max_length=120)),
                ("seat_category", models.CharField(max_length=50)),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("notes", models.TextField(blank=True)),
                ("purchased_at", models.DateTimeField(auto_now_add=True)),
                (
                    "race",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to="api.race",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tickets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="ticket",
            constraint=models.UniqueConstraint(
                fields=("user", "race", "ticket_holder_name", "seat_category"),
                name="unique_ticket_booking_per_user_race_holder_category",
            ),
        ),
    ]
