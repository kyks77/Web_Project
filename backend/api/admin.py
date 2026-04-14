from django.contrib import admin

from .models import Driver, Prediction, Race, Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "principal", "car_name", "created_at")
    search_fields = ("name", "country", "principal", "car_name")


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "nationality", "team", "podiums", "world_titles")
    list_filter = ("team", "nationality")
    search_fields = ("name",)


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ("grand_prix_name", "location", "race_date", "circuit_name", "laps")
    list_filter = ("race_date", "location")
    search_fields = ("grand_prix_name", "circuit_name", "location")


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ("user", "race", "predicted_winner", "predicted_pole", "created_at")
    list_filter = ("race", "user")
    search_fields = ("user__username", "race__grand_prix_name", "predicted_pole")

