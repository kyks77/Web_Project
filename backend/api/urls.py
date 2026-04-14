from django.urls import path

from . import views


urlpatterns = [
    # Auth
    path("auth/login/", views.login_view, name="login"),
    path("auth/logout/", views.logout_view, name="logout"),
    # Teams
    path("teams/", views.TeamListCreateAPIView.as_view(), name="team-list-create"),
    path("teams/<int:pk>/", views.TeamDetailAPIView.as_view(), name="team-detail"),
    # Drivers / Races (browse)
    path("drivers/", views.DriverListAPIView.as_view(), name="driver-list"),
    path("races/", views.RaceListAPIView.as_view(), name="race-list"),
    # Predictions (user-owned CRUD)
    path(
        "predictions/",
        views.PredictionListCreateAPIView.as_view(),
        name="prediction-list-create",
    ),
    path(
        "predictions/<int:pk>/",
        views.PredictionDetailAPIView.as_view(),
        name="prediction-detail",
    ),
    # Stats / summaries (function-based)
    path("stats/drivers/", views.driver_stats_view, name="driver-stats"),
    path("races/summary/", views.race_summary_view, name="race-summary"),
]

