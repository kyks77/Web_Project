from django.db.models import Count
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Driver, Race, Team, Ticket
from .serializers import (
    DriverModelSerializer,
    DriverStatsSerializer,
    LoginSerializer,
    RaceModelSerializer,
    RaceSummarySerializer,
    TeamModelSerializer,
    TicketModelSerializer,
)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def login_view(request):
    """
    Token-based login.
    Returns: access + refresh tokens (JWT).
    """
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]

    refresh = RefreshToken.for_user(user)
    return Response(
        {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "username": user.username,
        }
    )


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def logout_view(request):
    """
    JWT logout via refresh token blacklist.
    Client sends: { "refresh": "<token>" }
    """
    refresh_token = request.data.get("refresh")
    if not refresh_token:
        return Response(
            {"detail": "Refresh token is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        token = RefreshToken(refresh_token)
        token.blacklist()
    except Exception:
        return Response(
            {"detail": "Invalid refresh token."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    return Response({"detail": "Logged out successfully."})


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def race_summary_view(request):
    """
    Simple "standings-style" schedule summary.
    Optional query:
      - upcoming=true
    """
    upcoming = request.query_params.get("upcoming") == "true"
    qs = Race.objects.all()
    if upcoming:
        qs = qs.upcoming()

    data = [
        {
            "grand_prix_name": r.grand_prix_name,
            "race_date": r.race_date,
            "location": r.location,
            "circuit_name": r.circuit_name,
            "winner_driver_name": r.winner_driver.name if r.winner_driver else None,
        }
        for r in qs
    ]
    return Response(RaceSummarySerializer(data, many=True).data)


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def driver_stats_view(request):
    """
    Lightweight "standings-style" driver stats.
    """
    drivers = (
        Driver.objects.select_related("team")
        .annotate(wins=Count("wins"))
        .order_by("-world_titles", "-wins", "-podiums", "name")
    )
    data = [
        {
            "name": d.name,
            "team_name": d.team.name,
            "podiums": d.podiums,
            "world_titles": d.world_titles,
            "wins": d.wins,
        }
        for d in drivers
    ]
    return Response(DriverStatsSerializer(data, many=True).data)


class TeamListCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        teams = Team.objects.all().order_by("name")
        return Response(TeamModelSerializer(teams, many=True).data)

    def post(self, request):
        serializer = TeamModelSerializer(data=request.data)
        if serializer.is_valid():
            team = serializer.save()
            return Response(TeamModelSerializer(team).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeamDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk: int) -> Team:
        return Team.objects.get(pk=pk)

    def get(self, request, pk: int):
        try:
            team = self.get_object(pk)
        except Team.DoesNotExist:
            return Response({"detail": "Team not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(TeamModelSerializer(team).data)

    def put(self, request, pk: int):
        try:
            team = self.get_object(pk)
        except Team.DoesNotExist:
            return Response({"detail": "Team not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeamModelSerializer(team, data=request.data)
        if serializer.is_valid():
            team = serializer.save()
            return Response(TeamModelSerializer(team).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int):
        try:
            team = self.get_object(pk)
        except Team.DoesNotExist:
            return Response({"detail": "Team not found."}, status=status.HTTP_404_NOT_FOUND)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RaceListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        upcoming = request.query_params.get("upcoming") == "true"
        qs = Race.objects.select_related("winner_driver").all()
        if upcoming:
            qs = qs.upcoming()
        return Response(RaceModelSerializer(qs, many=True).data)


class DriverListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        drivers = Driver.objects.select_related("team").all().order_by("team__name", "number")
        return Response(DriverModelSerializer(drivers, many=True).data)


class TicketListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tickets = (
            Ticket.objects.select_related("race", "user")
            .filter(user=request.user)
            .order_by("-purchased_at")
        )
        return Response(TicketModelSerializer(tickets, many=True).data)

    def post(self, request):
        serializer = TicketModelSerializer(data=request.data)
        if serializer.is_valid():
            ticket = serializer.save(user=request.user)
            return Response(
                TicketModelSerializer(ticket).data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk: int, user):
        return Ticket.objects.select_related("race", "user").get(pk=pk, user=user)

    def get(self, request, pk: int):
        try:
            ticket = self.get_object(pk, request.user)
        except Ticket.DoesNotExist:
            return Response({"detail": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response(TicketModelSerializer(ticket).data)

    def put(self, request, pk: int):
        try:
            ticket = self.get_object(pk, request.user)
        except Ticket.DoesNotExist:
            return Response({"detail": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TicketModelSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            updated = serializer.save(user=request.user)
            return Response(TicketModelSerializer(updated).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int):
        try:
            ticket = self.get_object(pk, request.user)
        except Ticket.DoesNotExist:
            return Response({"detail": "Ticket not found."}, status=status.HTTP_404_NOT_FOUND)
        ticket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
