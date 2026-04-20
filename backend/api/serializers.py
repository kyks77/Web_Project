from django.contrib.auth import authenticate
from rest_framework import serializers

<<<<<<< HEAD
from .models import Driver, Prediction, Race, Team
=======
from .models import Driver, Race, Team, Ticket
>>>>>>> ticket-project-update


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


<<<<<<< HEAD
class PredictionModelSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source="user.username", read_only=True)
    race_detail = RaceModelSerializer(source="race", read_only=True)
    predicted_winner_detail = DriverModelSerializer(source="predicted_winner", read_only=True)
=======
class TicketModelSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source="user.username", read_only=True)
    race_detail = RaceModelSerializer(source="race", read_only=True)
>>>>>>> ticket-project-update

    race_id = serializers.PrimaryKeyRelatedField(
        source="race", queryset=Race.objects.all(), write_only=True
    )
<<<<<<< HEAD
    predicted_winner_id = serializers.PrimaryKeyRelatedField(
        source="predicted_winner", queryset=Driver.objects.all(), write_only=True
    )

    class Meta:
        model = Prediction
=======

    class Meta:
        model = Ticket
>>>>>>> ticket-project-update
        fields = [
            "id",
            "user",
            "user_username",
            "race",
            "race_id",
            "race_detail",
<<<<<<< HEAD
            "predicted_winner",
            "predicted_winner_id",
            "predicted_winner_detail",
            "predicted_pole",
            "notes",
            "created_at",
        ]
        read_only_fields = ["user", "race", "predicted_winner", "created_at"]
=======
            "ticket_holder_name",
            "seat_category",
            "quantity",
            "notes",
            "purchased_at",
        ]
        read_only_fields = ["user", "race", "purchased_at"]
>>>>>>> ticket-project-update


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
<<<<<<< HEAD

=======
>>>>>>> ticket-project-update
