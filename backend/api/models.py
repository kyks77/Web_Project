from django.conf import settings
from django.db import models
from django.utils import timezone


class Team(models.Model):
    name = models.CharField(max_length=120, unique=True)
    country = models.CharField(max_length=80)
    principal = models.CharField(max_length=120)
    car_name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=120)
    number = models.PositiveIntegerField()
    nationality = models.CharField(max_length=80)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="drivers")
    podiums = models.PositiveIntegerField(default=0)
    world_titles = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("name", "number")

    def __str__(self) -> str:
        return f"{self.name} #{self.number}"


class RaceQuerySet(models.QuerySet):
    def upcoming(self):
        return self.filter(race_date__gte=timezone.localdate()).order_by("race_date")


class Race(models.Model):
    grand_prix_name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    race_date = models.DateField()
    circuit_name = models.CharField(max_length=120)
    winner_driver = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wins",
    )
    laps = models.PositiveIntegerField()

    objects = RaceQuerySet.as_manager()

    class Meta:
        ordering = ["race_date"]
        unique_together = ("grand_prix_name", "race_date")

    def __str__(self) -> str:
        return f"{self.grand_prix_name} ({self.race_date})"


class Prediction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="predictions"
    )
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name="predictions")
    predicted_winner = models.ForeignKey(
        Driver, on_delete=models.CASCADE, related_name="predicted_winner_in"
    )
    predicted_pole = models.CharField(max_length=120)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "race"], name="unique_prediction_per_user_per_race"
            )
        ]

    def __str__(self) -> str:
        return f"Prediction by {self.user} for {self.race}"

