from django.contrib import admin

<<<<<<< HEAD
from .models import Driver, Prediction, Race, Team
=======
from .models import Driver, Race, Team, Ticket
>>>>>>> ticket-project-update


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


<<<<<<< HEAD
@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ("user", "race", "predicted_winner", "predicted_pole", "created_at")
    list_filter = ("race", "user")
    search_fields = ("user__username", "race__grand_prix_name", "predicted_pole")

=======
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "race",
        "ticket_holder_name",
        "seat_category",
        "quantity",
        "purchased_at",
    )
    list_filter = ("race", "user")
    search_fields = ("user__username", "race__grand_prix_name", "ticket_holder_name")
>>>>>>> ticket-project-update
