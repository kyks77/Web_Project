from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Driver, Race, Team, Ticket


class TeamModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "country", "principal", "car_name", "created_at"]


class DriverModelSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source="team.name", read_only=True)

    class Meta:
        model = Driver
        fields = [
            "id",
            "name",
            "number",
            "nationality",
            "team",
            "team_name",
            "podiums",
            "world_titles",
        ]


class RaceModelSerializer(serializers.ModelSerializer):
    winner_driver_name = serializers.CharField(source="winner_driver.name", read_only=True)

    class Meta:
        model = Race
        fields = [
            "id",
            "grand_prix_name",
            "location",
            "race_date",
            "circuit_name",
            "winner_driver",
            "winner_driver_name",
            "laps",
        ]


class TicketModelSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source="user.username", read_only=True)
    race_detail = RaceModelSerializer(source="race", read_only=True)

    race_id = serializers.PrimaryKeyRelatedField(
        source="race", queryset=Race.objects.all(), write_only=True
    )

    class Meta:
        model = Ticket
        fields = [
            "id",
            "user",
            "user_username",
            "race",
            "race_id",
            "race_detail",
            "ticket_holder_name",
            "seat_category",
            "quantity",
            "notes",
            "purchased_at",
        ]
        read_only_fields = ["user", "race", "purchased_at"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs.get("username"), password=attrs.get("password"))
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        attrs["user"] = user
        return attrs


class RaceSummarySerializer(serializers.Serializer):
    grand_prix_name = serializers.CharField()
    race_date = serializers.DateField()
    location = serializers.CharField()
    circuit_name = serializers.CharField()
    winner_driver_name = serializers.CharField(allow_null=True)


class DriverStatsSerializer(serializers.Serializer):
    name = serializers.CharField()
    team_name = serializers.CharField()
    podiums = serializers.IntegerField()
    world_titles = serializers.IntegerField()
    wins = serializers.IntegerField()
