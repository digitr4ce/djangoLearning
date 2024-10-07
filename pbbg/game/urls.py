from django.urls import path

from . import views

app_name = "game"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("player/<int:player_id>/", views.player, name="player"),
]
